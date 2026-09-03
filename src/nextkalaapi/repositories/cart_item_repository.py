from sqlalchemy import select

from nextkalaapi.models.cart_item_model import CartItem
from sqlalchemy.orm import Session


# read by id
def get_cart_item(db: Session, cart_item_id: int) -> CartItem | None:
    stmt = select(CartItem).where(CartItem.id == cart_item_id)
    return db.scalar(stmt)


# read all
def get_cart_items(db: Session) -> list[CartItem] | None:
    stmt = select(CartItem)
    return list(db.scalars(stmt).all())


# read by cart id
def get_cart_item_by_cart_id(db: Session, cart_id: int) -> list[CartItem] | None:
    stmt = select(CartItem).where(CartItem.cart_id == cart_id)

    return list(db.scalars(stmt).all())


# read by product id
def get_cart_item_by_product_id(db: Session, product_id: int) -> CartItem | None:
    stmt = select(CartItem).where(CartItem.product_id == product_id)

    return db.scalar(stmt)


# create
def create_cart_item(db: Session, cart_item: CartItem) -> CartItem:
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)

    return cart_item


# Update
def update_cart_item(db: Session, cart_item: CartItem) -> CartItem:
    db.refresh(cart_item)
    db.commit()

    return cart_item


# delete
def delete_cart_item(db: Session, cart_item_id: int) -> int | None:
    cart_item = get_cart_item(db, cart_item_id)
    if cart_item is None:
        return None
    db.delete(cart_item)
    db.commit()

    return cart_item_id
