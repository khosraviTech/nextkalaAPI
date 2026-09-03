from sqlalchemy.orm import Session, sessionmaker

from nextkalaapi.models.order_model import Order
from nextkalaapi.repositories import order_repository
from nextkalaapi.schemas.order import OrderInsert, OrderUpdate


# read
def get_order(db: Session, order_id: int) -> Order | None:
    return order_repository.get_order(db, order_id)


def get_orders(db: Session) -> list[Order] | None:
    return order_repository.get_orders(db)


# create
def create_order(db: Session, order_data: OrderInsert) -> Order:
    return order_repository.create_order(db, **order_data.model_dump())


# update
def update_order(db: Session, order_id: int, order_data: OrderUpdate) -> Order | None:
    order = order_repository.get_order(db, order_id)
    if order is None:
        return None
    update_data = order_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if field != "id":
            setattr(order, field, value)
    return order


# delete
def delete_order(db: Session, order_id: int) -> int | None:
    return order_repository.delete_order(db, order_id)
