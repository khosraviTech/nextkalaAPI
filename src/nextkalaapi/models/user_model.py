from enum import Enum

from sqlalchemy import Enum as SQLEnum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from nextkalaapi.models.base import Base


class Role(str, Enum):
    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, index=True, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[Role] = mapped_column(SQLEnum(Role), default=Role.USER, nullable=False)

    # nullable fields
    age: Mapped[int] = mapped_column(nullable=True)
    gender: Mapped[bool] = mapped_column(nullable=True)
    image: Mapped[str] = mapped_column(nullable=True)

    # relationships:
    # cart 1--1 user
    cart: Mapped["Cart"] = relationship(
        back_populates="user", cascade="all, delete-orphan", single_parent=True
    )
    # user 1--M order
    orders: Mapped[list["Order"]] = relationship(
        back_populates="user", cascade="all, delete-orphan" #user.remove(order)
    )  # now can use : user.order becase of back_populates
