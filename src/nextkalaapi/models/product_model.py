from enum import Enum


from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ARRAY, Enum as SQLEnum, String

from nextkalaapi.models.tag_model import Tag

class Base(DeclarativeBase):#alchemy db model
    pass

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int]=mapped_column(primary_key=True)
    title: Mapped[str]=mapped_column(nullable=False,String(100))
    description: Mapped[str]=mapped_column(nullable=False,String(300))
    category: Mapped[str] =mapped_column(nullable=False,String(50))
    price: Mapped[float]=mapped_column(nullable=False)
    brand: Mapped[str] =mapped_column(nullable=False)
    images: Mapped[list[str]] = mapped_column(
        ARRAY(String),
        nullable=False
    )

    discountPercentage: Mapped[float] =mapped_column(nullable=True)
    rating: Mapped[float] =mapped_column(nullable=True)
    tags: Mapped[list["Tag"]] = relationship(
        secondary="product_tags",
        back_populates="products"
    )
    weight: Mapped[float] =mapped_column(nullable=True)
    availabilityStatus: Mapped[str] =mapped_column(nullable=True)
    returnPolicy: Mapped[str] =mapped_column(nullable=True)
    minimumOrderQuantity: Mapped[int] =mapped_column(nullable=True)
    thumbnail: Mapped[str] =mapped_column(nullable=True)



