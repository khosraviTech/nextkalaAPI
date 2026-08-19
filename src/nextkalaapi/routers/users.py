from fastapi import APIRouter

router = APIRouter()

@router.get("userId/", )#select a user by userID
async def read_user():
    pass