from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from nextkalaapi.models.base import Base


class Cart(Base):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(primary_key=True)

    # relationships:

    # cart 1--1 user
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        unique=True,
    )
    user: Mapped["User"] = relationship(back_populates="cart", single_parent=True)

    # cart 1--M cartItem
    cart_items: Mapped[list["CartItem"]] = relationship(
         cascade="all, delete"
    )
    
