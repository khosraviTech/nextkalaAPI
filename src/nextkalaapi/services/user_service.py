from sqlalchemy.orm import Session

from nextkalaapi.models.user_model import User
from nextkalaapi.repositories import user_repository
from nextkalaapi.schemas.user import UserInsert, UserUpdate


# read
def get_user(db: Session, user_id: int) -> User | None:
    return user_repository.get_user(db, user_id)


def get_users(db: Session) -> list[User]:
    return user_repository.get_users(db)


# create
def create_user(db: Session, user_data: UserInsert) -> User:
    user = User(**user_data.model_dump())

    return user_repository.create_user(db, user)


# update
def update_user(
    db: Session,
    user_id: int,
    user_data: UserUpdate,
) -> User | None:

    user = user_repository.get_user(db, user_id)

    if user is None:
        return None

    update_data = user_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        if field != "id":
            setattr(user, field, value)

    return user_repository.update_user(db, user)


# delete
def delete_user(db: Session, user_id: int) -> int | None:
    return user_repository.delete_user(db, user_id)