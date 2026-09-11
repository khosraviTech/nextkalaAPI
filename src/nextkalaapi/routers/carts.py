from fastapi import APIRouter, Depends, HTTPException, status
from psycopg.errors import DependentPrivilegeDescriptorsStillExist
from sqlalchemy.orm import Session

from nextkalaapi.database import get_db
from nextkalaapi.models.cart_model import Cart
from nextkalaapi.schemas.cart import CartInsert, CartRow
from nextkalaapi.services import cart_service

router = APIRouter()

# create
@router.post("/create", response_model=CartRow)
def create_cart(cart_data: CartInsert, db: Session = Depends(get_db)):
    cart = cart_service.create_cart(db, cart_data)
    if cart is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="cart cratione faild!"
        )
    return cart
