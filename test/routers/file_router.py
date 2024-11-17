from fastapi import APIRouter, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import re

# Initialize router and templates
router = APIRouter(prefix="/file_upload", tags=["Upload File"])
templates = Jinja2Templates(directory="templates")


def clean_text(content: str) -> str:
    # Clean and format the content of the file
    content = content.decode("utf-8")
    # content = re.sub(r"\r\n", "\n", content)  # Standardize newlines
    # content = re.sub(r"\t", "    ", content)  # Replace tabs with spaces
    # content = re.sub(r"\*\*\*", "", content)  # Remove extra characters
    # content = re.sub(r"(\d+)\.(\w)", r"\1. \2", content)  # Space after numbers
    # content = re.sub(r"(\n{2,})", "\n\n", content)  # Remove extra newlines
    # content = re.sub(r"\n\n    ", "\n    ", content)  # Standardize indentation
    # content = re.sub(r"(\n)([A-Za-z ]+:)", r"\1\n\2", content)  # Headers spacing
    return content


@router.get("/", response_class=HTMLResponse)
async def get_upload_form(request: Request):
    # Render the upload form
    return templates.TemplateResponse("upload.html", {"request": request})


@router.post("/", response_class=HTMLResponse)
async def upload_file(request: Request, uploaded_file: UploadFile = File(...)):
    # Read and clean the file content
    content = await uploaded_file.read()
    cleaned_content = clean_text(content)
    return templates.TemplateResponse(
        "upload.html", {"request": request, "cleaned_content": cleaned_content}
    )
