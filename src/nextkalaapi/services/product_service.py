from sqlalchemy.orm import Session

from nextkalaapi.models.product_model import Product
from nextkalaapi.repositories import product_repository
from nextkalaapi.schemas.product import ProductInsert, ProductUpdate


# read
def get_product(db: Session, product_id: int) -> Product | None:
    return product_repository.get_product(db, product_id)


# create
def create_product(db: Session, product_data: ProductInsert) -> Product:
    return product_repository.create_product(db, **product_data.model_dump())


# update
def update_product(
    db: Session, product_id: int, product_data: ProductUpdate
) -> Product | None:

    product = product_repository.get_product(db, product_id)
    if product is None:
        return None

    update_data = product_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if field != "id":
            setattr(product, field, value)

    return product_repository.update_product(db, product)


# delete
def delete_product(db: Session, product_id: int) -> int | None:
    return product_repository.delete_product(db, product_id)
