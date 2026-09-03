from sqlalchemy.orm import Session

from nextkalaapi.models.cart_item_model import CartItem
from nextkalaapi.repositories import cart_item_repository
from nextkalaapi.schemas.cart_item import CartItemInsert, CartItemUpdate


# read by cart id
def get_cart_item_by_cart_id(db: Session, cart_id: int) -> list[CartItem] | None:
    return cart_item_repository.get_cart_item_by_cart_id(db, cart_id)


# create
def create_cart_item(db: Session, cart_item: CartItemInsert) -> CartItem:
    return cart_item_repository.create_cart_item(db, **cart_item.model_dump())


# update
def update_cart_item(
    db: Session, cart_item_id: int, cart_item_data: CartItemUpdate
) -> CartItem | None:
    cart_item = cart_item_repository.get_cart_item(db, cart_item_id)
    if cart_item is None:
        return None
    update_data = cart_item_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if field!="id":
            setattr(cart_item, field, value)
    return cart_item


# delete
def delete_cart_item(db: Session, cart_item_id: int) -> int | None:
    return cart_item_repository.delete_cart_item(db, cart_item_id)
