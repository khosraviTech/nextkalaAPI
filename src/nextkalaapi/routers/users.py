from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from nextkalaapi.database import get_db
from nextkalaapi.schemas.user import UserDelete, UserInsert, UserRow, UserSchema, UserUpdate
from nextkalaapi.services import user_service

router = APIRouter()


# read user by id
@router.get("/user_id/{user_id}", response_model=UserRow)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user(db, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User by id {user_id} not found",
        )

    return user


# read all users
@router.get("/all", response_model=list[UserRow])
def read_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)

# create user
@router.post(
    "/create",
    response_model=UserRow,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_data: UserInsert,
    db: Session = Depends(get_db),
):
    return user_service.create_user(db,user_data)

# update user
@router.patch(
    "/update/user_id/{user_id}",
    response_model=UserRow,

)
def update_user(
    user_id:int,
    user_data:UserUpdate,
    db:Session=Depends(get_db)
):
    user = user_service.update_user(db,user_id,user_data)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User by id {user_id} not found",
        )
    return user

@router.delete(
    "/delete/user_id/{user_id}",
    response_model=UserDelete
)
def delete_user(
    user_id:int,
    db:Session=Depends(get_db)
    
):
    user = user_service.delete_user(db,user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User by id {user_id} not found",
        )
    return {"id": user}
    