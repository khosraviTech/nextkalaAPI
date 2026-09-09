from fastapi import APIRouter, Depends, HTTPException, status
from httptools import HttpParserCallbackError
from sqlalchemy.orm import Session

from nextkalaapi.database import get_db
from nextkalaapi.schemas.order import OrderInsert, OrderRow
from nextkalaapi.services import order_item_service, order_service

router = APIRouter()


# read
@router.get("/order_id/{order_id}", response_model=OrderRow)
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = order_service.get_order(db, order_id)
    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"order by id {order_id} not found!",
        )
    return order


