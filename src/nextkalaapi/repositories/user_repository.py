
from sqlalchemy import select
from sqlalchemy.orm import Session

from nextkalaapi.models.user_model import User


# read
def get_user(db: Session, user_id: int) -> User | None:
    stmt = select(User).where(User.id == user_id)
    return db.scalar(stmt)


def get_users(db: Session) -> list[User]:
    stmt = select(User)
    return list(db.scalars(stmt).all())


# create
def create_user(db: Session, user: User) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# update
def update_user(
    db: Session, user: User
) -> (
    User
):  # changes will happen in Service layer: user_repository.update_user(db, user)
    db.refresh(user)
    db.commit()
    return user


# delete
def delete_user(db: Session, user_id: int) -> int | None:
    user = get_user(db, user_id)

    if user is None:
        return None

    db.delete(user)
    db.commit()

    return user_id
