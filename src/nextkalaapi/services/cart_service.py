from sqlalchemy import update
from sqlalchemy.orm import Session

from nextkalaapi.models.cart_model import Cart
from nextkalaapi.repositories import cart_repository
from nextkalaapi.schemas import cart


# read
def get_cart(db: Session, cart_id: int) -> Cart | None:
    return cart_repository.get_cart(db, cart_id)


# read all
def get_carts(db: Session) -> list[Cart] | None:
    return cart_repository.get_carts(db)


# create
def create_cart(db: Session, cart_data: cart.CartInsert) -> Cart:
    return cart_repository.create_cart(db, **cart_data.model_dump())


# update
def update_cart(db: Session, cart_id: int, cart_data: cart.CartUpdate) -> Cart | None:
    cart = cart_repository.get_cart(db, cart_id)
    if cart is None:
        return None
    update_data = cart_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if field != "id":
            setattr(cart, field, value)
    return cart


# delete
def delete_cart(db: Session, cart_id: int) -> int | None:
    return cart_repository.delete_cart(db, cart_id)
