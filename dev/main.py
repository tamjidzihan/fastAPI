from fastapi import (
    FastAPI,
    WebSocket,
    WebSocketDisconnect,
    BackgroundTasks,
    UploadFile,
    File,
)
from fastapi.responses import HTMLResponse
from motor.motor_asyncio import AsyncIOMotorClient
from pathlib import Path
import openai
import os
import uuid
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Set up MongoDB
client = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
db = client.translation_service

# LLM API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}


# Background task for file processing
async def process_translation(file_path: str, language: str, session_id: str):
    try:
        # Read file content
        with open(file_path, "r") as file:
            content = file.read()

        # Request translation from LLM
        translated = await translate_text(content, language)

        # Save translated file
        translated_path = f"translated_{session_id}.txt"
        with open(translated_path, "w") as file:
            file.write(translated)

        # Store result in MongoDB
        await db.history.insert_one(
            {
                "sessionId": session_id,
                "fileName": file_path,
                "processedAt": str(uuid.uuid4()),
                "result": translated,
            }
        )
    except Exception as e:
        print(f"Error during translation: {e}")


async def translate_text(content: str, language: str) -> str:
    # Use OpenAI or another LLM API for translation
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Translate the following text to {language}: {content}",
        temperature=0.3,
        max_tokens=1000,
    )
    return response.choices[0].text.strip()


# WebSocket for real-time status updates
@app.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await websocket.accept()
    try:
        # Send initial status
        await websocket.send_text("File received, processing...")

        # Wait for translation to complete
        while True:
            await websocket.send_text("Translating...")
            # Simulate real-time update, process the translation
            await process_translation("path/to/file", "fr", session_id)
            await websocket.send_text("Translation complete. Download available.")
            break
    except WebSocketDisconnect:
        print(f"Client {session_id} disconnected")


# File upload endpoint
@app.post("/upload/")
async def upload_file(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    language: str = "en",
):
    session_id = str(uuid.uuid4())
    file_path = f"uploaded_{session_id}.txt"

    # Save the uploaded file temporarily
    with open(file_path, "wb") as f:
        f.write(await file.read())

    background_tasks.add_task(process_translation, file_path, language, session_id)

    return {"session_id": session_id, "message": "File uploaded, translation started."}


# Frontend HTML rendering
@app.get("/", response_class=HTMLResponse)
async def get_form():
    with open("templates/index.html", "r") as file:
        return file.read()


# Serve static files (CSS, JS)
@app.get("/static/{file_name}")
async def serve_static(file_name: str):
    return Path(f"static/{file_name}").read_text()
