from datetime import UTC, datetime
from enum import Enum

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from nextkalaapi.models.base import Base
from nextkalaapi.models.order_item_model import OrderItem


class OrderStatus(str, Enum):
    processing = "processing"
    cancelled = "cancelled"
    shipped = "shipped"
    delivered = "delivered"


class PaymentStatus(str, Enum):
    pending = "pending"
    paid = "paid"
    failed = "failed"


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(nullable=False, primary_key=True)

    subtotal: Mapped[int] = mapped_column(nullable=False)
    shipping: Mapped[int] = mapped_column(nullable=False)
    tax: Mapped[int] = mapped_column(nullable=False)
    total: Mapped[int] = mapped_column(nullable=False)
    paymentStatus: Mapped[PaymentStatus] = mapped_column(default=PaymentStatus.pending)
    orderStatus: Mapped[OrderStatus] = mapped_column(default=OrderStatus.processing)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )
    # relationships:
    # order 1--M orderItem
    order_items: Mapped[list[OrderItem]] = relationship(
        cascade="all , delete-orphan",back_populates="order" #delete-orphan: It means I can use order.order_items.remove(item)
    )
    # user 1--M order
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )
    user: Mapped["User"] = relationship(back_populates="orders") # now can use : order.user becase of back_populates
