from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import user_router, file_router
from models import models
from db.database import engine


models.Base.metadata.create_all(engine)


app = FastAPI()

# app.include_router(user_router.router)
app.include_router(file_router.router)


@app.get("/", tags=["home"])
def index():
    return {"message": "test API"}


# CORS configuration (customize origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
