from sqlalchemy import ARRAY, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from nextkalaapi.models.base import Base
from nextkalaapi.models.products_tags_table import products_tags_table


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(300), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    brand: Mapped[str] = mapped_column(nullable=False)
    images: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=False)
    
    # relationships:
    # product 1--M cartItem
    cart_items: Mapped[list["CartItem"]] = relationship(cascade="all , delete")

    # product 1--M orderItem
    order_items: Mapped[list["OrderItem"]] = relationship(back_populates="product") #product.order_items 

    # product M--M tag
    tags: Mapped[list["Tag"]] = relationship(secondary=products_tags_table,back_populates="products")
