from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from nextkalaapi.models.base import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int] = mapped_column(nullable=False)
    product_title:Mapped[str]=mapped_column(String(100),nullable=False)

    # relationships:
    # cart 1--M cartItem
    cart_id: Mapped[int] = mapped_column(ForeignKey("carts.id"), nullable=False)
    cart: Mapped["Cart"] = relationship(back_populates="cart_items")
    # product 1--M cartItem
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
