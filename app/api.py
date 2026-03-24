from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {
        "message": "AI Legal Intelligence Platform is running successfully"
    }
