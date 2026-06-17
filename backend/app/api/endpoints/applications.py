from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_application():
    return {"message": "Application created"}

@router.get("/")
async def get_applications():
    return {"applications": []}
