from fastapi import APIRouter, Depends
from sqlalchemy import null
from sqlalchemy.orm import Session

from nextkalaapi.database import get_db
from nextkalaapi.schemas.product import ProductRow
from nextkalaapi.services import product_service

router = APIRouter()


# read all
@router.get("/all", response_model=list[ProductRow])
def read_products(db: Session = Depends(get_db)):
    products = product_service.get_products(db)
    return products
# read by id
@router.get("/product_id/{product_id}",response_model=ProductRow)
def read_product(
    product_id:int,
    db:Session=Depends(get_db)
):
    return product_service.get_product(db,product_id)

