
from sqlalchemy import select
from sqlalchemy.orm import Session

from nextkalaapi.models.cart_model import Cart


# read by id
def get_cart(db: Session, cart_id: int) -> Cart | None:
    stmt = select(Cart).where(Cart.id == cart_id)
    return db.scalar(stmt)


# read by user id
def get_cart_by_user_id(db: Session, user_id: int) -> Cart | None:
    stmt = select(Cart).where(Cart.user_id == user_id)
    return db.scalar(stmt)


# read all
def get_carts(db: Session) -> list[Cart]:
    stmt = select(Cart)
    return list(db.scalars(stmt).all())


# create
def create_cart(db: Session, cart: Cart) -> Cart:
    db.add(cart)
    db.commit()
    db.refresh(cart)

    return cart


# update
def update_cart(db: Session, cart: Cart) -> Cart:
    db.commit()
    db.refresh(cart)
    

    return cart


# delete
def delete_cart(db: Session, cart_id: int) -> int | None:
    cart = select(Cart).where(Cart.id == cart_id)
    if cart is None:
        return None
    db.delete(cart)
    db.commit()
    return cart_id
