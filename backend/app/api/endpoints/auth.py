from fastapi import APIRouter

router = APIRouter()

@router.post("/signup")
async def signup():
    return {"message": "Signup logic here"}

@router.post("/login")
async def login():
    return {"message": "Login logic here"}
