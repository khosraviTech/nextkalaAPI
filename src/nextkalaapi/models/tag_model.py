from enum import Enum


from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Enum as SQLEnum, String

from nextkalaapi.models.product_model import Product

class Base(DeclarativeBase):#alchemy db model
    pass

class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )

    products: Mapped[list["Product"]] = relationship(
        secondary="product_tags",
        back_populates="tags"
    )