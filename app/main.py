from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.api_v1_router import api_router

load_dotenv()

app = FastAPI(title=os.getenv("PROJECT_NAME", "Developer Toolbox API"))

# Register API routes
app.include_router(api_router, prefix=os.getenv("API_V1_STR", "/api/v1"))

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "👑 Welcome to Developer Toolbox API"}
