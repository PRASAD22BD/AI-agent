from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_jobs():
    return {"jobs": []}

@router.post("/match")
async def match_jobs():
    return {"matches": []}
