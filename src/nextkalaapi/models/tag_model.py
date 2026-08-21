
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from nextkalaapi.models.base import Base
from nextkalaapi.models.product_model import Product


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )

    products: Mapped[list[Product]] = relationship(
        secondary="product_tags",
        back_populates="tags"
    )