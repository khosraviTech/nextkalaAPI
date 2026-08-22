from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from nextkalaapi.models.product_model import Product


from nextkalaapi.models.base import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    quantity: Mapped[int] = mapped_column(nullable=False)

    # relationships:
    # cart 1--M cartItem
    cart_id: Mapped[int] = mapped_column(ForeignKey("carts.id"), nullable=False)

    # product 1--M cartItem
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
