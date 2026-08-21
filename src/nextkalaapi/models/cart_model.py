from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from nextkalaapi.models.base import Base
from nextkalaapi.models.cart_item_model import CartItem
from nextkalaapi.models.user_model import User


class Cart(Base):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    items: Mapped[list["CartItem"]] = relationship(
        back_populates="cart", cascade="all, delete-orphan"
    )
    user:Mapped["User"] = relationship(back_populates="cart")
