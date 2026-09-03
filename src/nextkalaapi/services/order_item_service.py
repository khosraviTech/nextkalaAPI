from sqlalchemy.orm import Session

from nextkalaapi.models.order_item_model import OrderItem
from nextkalaapi.repositories import order_item_repository
from nextkalaapi.schemas.order_item import OrderItemInsert, OrderItemUpdate


# read all order items with order id
def get_order_item_by_order_id(db: Session, order_id: int) -> list[OrderItem] | None:
    return order_item_repository.get_order_item_by_order_id(db, order_id)


# create
def create_order_item(db: Session, order_item: OrderItemInsert):
    return order_item_repository.create_order_item(db, **order_item.model_dump())


# update
def update_order_item(
    db: Session, order_item_id: int, order_item_data: OrderItemUpdate
) -> OrderItem | None:
    order_item = order_item_repository.get_order_item(db, order_item_id)
    if order_item is None:
        return None
    update_data = order_item_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if field != "id":
            setattr(order_item, field, value)
    return order_item


# delete
def delete_order_item(db: Session, order_item_id: int) -> int | None:
    return order_item_repository.delete_order_item(db, order_item_id)
