from pydantic import PositiveInt
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String



from nextkalaapi.models.base import Base

class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    unit_price: Mapped[PositiveInt] = mapped_column(nullable=False)
    quantity: Mapped[PositiveInt] = mapped_column(nullable=False)
    total_price: Mapped[PositiveInt] = mapped_column(nullable=False)
    
    
   
   
    # relationships:
    # product 1--M orderItem
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False, index=True)
    product:Mapped['Product'] = relationship(back_populates='order_items') #order_item.product
    # order 1--M orderItem
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False,index=True)
    order: Mapped["Order"] = relationship(back_populates="order_items") #order_item.order