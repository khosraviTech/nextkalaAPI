from pydantic import PositiveInt
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String



from nextkalaapi.models.base import Base

class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[PositiveInt] = mapped_column(nullable=False)
    quantity: Mapped[PositiveInt] = mapped_column(nullable=False)
    total_item_price: Mapped[PositiveInt] = mapped_column(nullable=False)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)
    product_id: Mapped[int] = (
        mapped_column(  # it must have a product id because order item is related to one product
            ForeignKey("products.id"), nullable=False
        )
    )
    product: Mapped["Product"] = relationship(  # just related to one product
        back_populates="order_items"
    )
    order: Mapped["Order"] = relationship(  # just related to one order
        back_populates="items",
    )
