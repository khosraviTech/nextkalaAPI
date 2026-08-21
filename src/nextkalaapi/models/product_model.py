from sqlalchemy import ARRAY, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .product_tags_model import product_tags
from nextkalaapi.models.base import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(300), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    brand: Mapped[str] = mapped_column(nullable=False)
    images: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)

    discountPercentage: Mapped[float] = mapped_column(nullable=True)
    rating: Mapped[float] = mapped_column(nullable=True)
    weight: Mapped[float] = mapped_column(nullable=True)
    availabilityStatus: Mapped[str] = mapped_column(nullable=True)
    returnPolicy: Mapped[str] = mapped_column(nullable=True)
    minimumOrderQuantity: Mapped[int] = mapped_column(nullable=True)
    thumbnail: Mapped[str] = mapped_column(nullable=True)

    tags: Mapped[list["Tag"]] = relationship(
        secondary=product_tags, back_populates="products"
    )
    cart_items: Mapped[list["CartItem"]] = relationship(back_populates="product")
    order_items: Mapped[list["OrderItem"]] = relationship(back_populates="product")
