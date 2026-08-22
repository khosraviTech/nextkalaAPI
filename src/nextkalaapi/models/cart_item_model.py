from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from nextkalaapi.models.product_model import Product


from nextkalaapi.models.base import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    totalItemPrice: Mapped[int] = mapped_column(nullable=False)

    product: Mapped[Product] = relationship(back_populates="cart_items")

    # relationships:
    # cart 1--M cartItem
    cart_id: Mapped[int] = mapped_column(ForeignKey("carts.id"), nullable=False)
    
