from sqlalchemy import select
from sqlalchemy.orm import Session

from nextkalaapi.models.order_item_model import OrderItem


# read by id
def get_order_item(db: Session, order_item_id: int) -> OrderItem | None:
    stmt = select(OrderItem).where(OrderItem.id == order_item_id)
    return db.scalar(stmt)


# read all
def get_order_items(db: Session) -> list[OrderItem] | None:
    stmt = select(OrderItem)
    return list(db.scalars(stmt).all())


# read by order id
def get_order_item_by_order_id(db: Session, order_id: int) -> list[OrderItem] | None:
    stmt = select(OrderItem).where(OrderItem.order_id == order_id)
    return list(db.scalars(stmt).all())


# read by product id
def get_order_item_by_product_id(db: Session, product_id: int) -> OrderItem | None:
    stmt = select(OrderItem).where(OrderItem.product_id == product_id)
    return db.scalar(stmt)


# create
def create_order_item(db: Session, order_item: OrderItem) -> OrderItem:
    db.add(order_item)
    db.commit()
    db.refresh(order_item)
    return order_item


# update
def update_order_item(db: Session, order_item: OrderItem) -> OrderItem:
    db.commit()
    db.refresh(order_item)
    

    return order_item


# delete
def delete_order_item(db: Session, order_item_id: int) -> int | None:
    order_item = get_order_item(db, order_item_id)
    if order_item is None:
        return None
    db.delete(order_item)
    db.commit()
    return order_item_id
