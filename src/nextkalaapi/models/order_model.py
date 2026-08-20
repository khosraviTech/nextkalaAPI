from enum import Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ARRAY, Enum as SQLEnum, Mapped[str]ing
from nextkalaapi.models.tag_model import Tag
from datetime import datetime
from zoneinfo import ZoneInfo
from sqlalchemy import DateTime

class Base(DeclarativeBase):#alchemy db model
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
    id: Mapped[Mapped[int]]=mapped_column(nullable=False,primary_key=True)
    userName: Mapped[str]=mapped_column(String(200),nullable=False)
    userEmail: Mapped[str]=mapped_column(String(200),nullable=False)
# TODO:cartItem or orderitem model for this problem of db design
    items: list[CartItem]=mapped_column(nullable=False)
    subtotal: Mapped[int]=mapped_column(nullable=False)
    shipping: Mapped[int]=mapped_column(nullable=False)
    tax: Mapped[int]=mapped_column(nullable=False)
    total: Mapped[int]=mapped_column(nullable=False)
    paymentStatus: Mapped[PaymentStatus] =mapped_column(default=PaymentStatus.pending) 
    orderStatus: Mapped[OrderStatus] =mapped_column(default=OrderStatus.processing) 
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(IRAN_TIMEZONE),
        nullable=False,
    )

    pass