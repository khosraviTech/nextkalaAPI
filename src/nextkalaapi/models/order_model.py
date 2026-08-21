from enum import Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ARRAY, Enum as SQLEnum, Mapped, String
from nextkalaapi.models.order_item_model import OrderItem
from nextkalaapi.models.tag_model import Tag
from datetime import UTC, datetime
from zoneinfo import ZoneInfo
from sqlalchemy import DateTime


class Base(DeclarativeBase):  # alchemy db model
    pass


class OrderStatus(Mapped[str], Enum):
    processing = "processing"
    cancelled = "cancelled"
    shipped = "shipped"
    delivered = "delivered"


class PaymentStatus(Mapped[str], Enum):
    pending = "pending"
    paid = "paid"
    failed = "failed"


class Order(Base):
    __tablename__ = "orders"
    id: Mapped[Mapped[int]] = mapped_column(nullable=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(nullable=False)
    # TODO:cartItem or orderitem model for this problem of db design
    items: Mapped[list[OrderItem]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan",
    )
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

    pass
