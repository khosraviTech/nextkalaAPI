
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .product_tags_model import product_tags
from nextkalaapi.models.base import Base



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
        secondary=product_tags,
        back_populates="tags"
    )