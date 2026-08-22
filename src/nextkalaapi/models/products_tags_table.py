from sqlalchemy import Column, ForeignKey, Table

from nextkalaapi.models.base import Base

products_tags_table = Table(
    "products_tags_table",
    Base.metadata,
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)
