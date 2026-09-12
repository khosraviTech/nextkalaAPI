from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from nextkalaapi.database import get_db
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

# read
@router.get("/cart_id/{cart_id}", response_model=CartRow)
def read_cart(cart_id: int, db: Session = Depends(get_db)):
    cart = cart_service.get_cart(db, cart_id)
    if cart is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"cart by id {cart_id} not found!",
        )
    return cart

# read all
@router.get("/all", response_model=list[CartRow])
def read_carts( db: Session = Depends(get_db)):
    cart = cart_service.get_carts(db)
    if cart is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"there is no cart!",
        )
    return cart
