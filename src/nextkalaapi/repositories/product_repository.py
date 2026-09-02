from sqlalchemy import select
from sqlalchemy.orm import Session

from nextkalaapi.models.product_model import Product


# read
def get_product(db: Session, product_id) -> Product | None:
    stmt = select(Product).where(Product.id == product_id)
    return db.scalar(stmt)


def get_products(db: Session) -> list[Product]:
    stmt = select(Product)
    return list(db.scalars(stmt).all())


# create
def create_product(db: Session, product: Product) -> Product:
    db.add(product)
    db.commit()
    db.refresh(product)

    return product


# update
def update_product(db: Session, product: Product) -> Product:
    db.refresh(product)
    db.commit()

    return product


# delete
def delete_product(db: Session, product_id: int) -> int | None:
    product = get_product(db, product_id)
    if not product:
        return None
    db.delete(product)
    db.commit()
    return product_id
