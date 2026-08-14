from enum import Enum
from typing import Annotated
from pydantic import BaseModel

from schemas.cart_item import CartItem


class OrderStatus(str, Enum):
    pending = "processing"
    cancelled = "cancelled"
    shipped = "shipped"
    delivered = "delivered"


class PaymentStatus(str, Enum):
    pending = "pending"
    paid = "paid"
    failed = "failed"


class OrderBase(BaseModel):
    orderId: str
    userName: str
    userEmail: str
    items: list[CartItem]
    subtotal: int
    shipping: int
    tax: str
    total: int
    paymentStatus: PaymentStatus
    orderStatus: OrderStatus
    createdAt: str
