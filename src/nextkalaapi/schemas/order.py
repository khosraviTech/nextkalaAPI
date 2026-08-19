from enum import Enum
from typing import Annotated
from pydantic import BaseModel

from nextkalaapi.schemas.cart_item import CartItem

class OrderStatus(str, Enum):
    processing = "processing"
    cancelled = "cancelled"
    shipped = "shipped"
    delivered = "delivered"


class PaymentStatus(str, Enum):
    pending = "pending"
    paid = "paid"
    failed = "failed"






# order update: there is no editing order in nextkala site 

# order create
class OrderCreate(BaseModel):
    orderId: str
    userName: str
    userEmail: str
    items: list[CartItem]
    subtotal: int
    shipping: int
    tax: str
    total: int
    paymentStatus: PaymentStatus = PaymentStatus.pending
    orderStatus: OrderStatus = OrderStatus.processing
    createdAt: str

# order response (read & delete)
class OrderResponse(OrderCreate):
    pass