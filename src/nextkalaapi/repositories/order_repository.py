from psycopg.errors import SerializationFailure
from sqlalchemy import select
from sqlalchemy.orm import Session

from nextkalaapi.models.order_model import Order


# read
def get_order(db: Session, order_id: int) -> Order | None:
    stmt = select(Order).where(Order.id == order_id)
    return db.scalar(stmt)


def get_orders(db: Session) -> list[Order] | None:
    stmt = select(Order)
    return list(db.scalars(stmt).all())


# create
def create_order(db: Session, order: Order) -> Order:
    db.add(order)
    db.commit()
    db.refresh(order)

    return order


# update
def update_order(db: Session, order: Order) -> Order:
    db.refresh(order)
    db.commit()

    return order


# delete
def delete_order(db: Session, order_id: int) -> int | None:
    order = get_order(db, order_id)

    if order is None:
        return None
    
    db.delete(order)
    db.commit()

    return order_id
