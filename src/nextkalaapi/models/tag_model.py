from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from nextkalaapi.models.base import Base

from .products_tags_table import products_tags_table


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False, index=True
    )

    # relationships:
    # product M--M tag
    products: Mapped[list["Product"]] = relationship(
        secondary= products_tags_table, back_populates="tags"
    )
