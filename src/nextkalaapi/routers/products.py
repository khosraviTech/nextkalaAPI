from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from nextkalaapi.database import get_db
from nextkalaapi.schemas.product import (
    ProductDelete,
    ProductInsert,
    ProductRow,
    ProductUpdate,
)
from nextkalaapi.services import product_service

router = APIRouter()


# read all
@router.get("/all", response_model=list[ProductRow])
def read_products(db: Session = Depends(get_db)):
    products = product_service.get_products(db)
    return products


# read by id
@router.get("/product_id/{product_id}", response_model=ProductRow)
def read_product(product_id: int, db: Session = Depends(get_db)):
    return product_service.get_product(db, product_id)


# create
@router.post(
    "/create",
    response_model=ProductRow,
    status_code=status.HTTP_201_CREATED,
)
def create_product(product_data: ProductInsert, db: Session = Depends(get_db)):
    return product_service.create_product(db, product_data)


# update
@router.patch("/update/product_id/{product_id}", response_model=ProductRow)
def update_product(
    product_id: int, product_data: ProductUpdate, db: Session = Depends(get_db)
):
    product = product_service.update_product(db,product_id,product_data)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product by id {product_id} not found",
        )
    return product


# delete
@router.delete("/delete/product_id/{product_id}", response_model=ProductDelete)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = product_service.delete_product(db, product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product by id {product_id} not found",
        )

    return {"id": product}
