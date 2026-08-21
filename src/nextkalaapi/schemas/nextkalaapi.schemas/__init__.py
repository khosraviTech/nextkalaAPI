"""Auto-generated Pydantic schemas"""

__all__ = [
    "CartItemSchema",
    "CartItemRow",
    "CartItemInsert",
    "CartItemUpdate",
    "CartSchema",
    "CartRow",
    "CartInsert",
    "CartUpdate",
    "OrderItemSchema",
    "OrderItemRow",
    "OrderItemInsert",
    "OrderItemUpdate",
    "OrderSchema",
    "OrderRow",
    "OrderInsert",
    "OrderUpdate",
    "ProductSchema",
    "ProductRow",
    "ProductInsert",
    "ProductUpdate",
    "TagSchema",
    "TagRow",
    "TagInsert",
    "TagUpdate",
    "UserSchema",
    "UserRow",
    "UserInsert",
    "UserUpdate",
]

from .cart_item import CartItemInsert, CartItemRow, CartItemSchema, CartItemUpdate
from .cart import CartInsert, CartRow, CartSchema, CartUpdate
from .order_item import OrderItemInsert, OrderItemRow, OrderItemSchema, OrderItemUpdate
from .order import OrderInsert, OrderRow, OrderSchema, OrderUpdate
from .product import ProductInsert, ProductRow, ProductSchema, ProductUpdate
from .tag import TagInsert, TagRow, TagSchema, TagUpdate
from .user import UserInsert, UserRow, UserSchema, UserUpdate

# Rebuild forward refs on all BaseModel subclasses
CartItemRow.model_rebuild()
CartRow.model_rebuild()
OrderItemRow.model_rebuild()
OrderRow.model_rebuild()
ProductRow.model_rebuild()
TagRow.model_rebuild()
UserRow.model_rebuild()
