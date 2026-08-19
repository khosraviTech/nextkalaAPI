from typing import Annotated
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from nextkalaapi.database import get_db
from nextkalaapi.schemas.user import UserResponse

router = APIRouter()

# TODO:implimetn read_user route handler
@router.get(  # select a user by userID
    "userId/{user_Id}", response_model=UserResponse, status_code=status.HTTP_302_FOUND
)
async def read_user(
    user_id:int,
    db:Annotated[Session, Depends(get_db)]
):
    pass
