from fastapi import APIRouter, Depends, HTTPException, status
from httptools import HttpParserCallbackError
from sqlalchemy.orm import Session

from nextkalaapi.database import get_db
from nextkalaapi.schemas import order
from nextkalaapi.schemas.order import OrderDelete, OrderInsert, OrderRow, OrderUpdate
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


# read all
@router.get("/all", response_model=list[OrderRow])
def read_orders(db: Session = Depends(get_db)):
    return order_service.get_orders(db)


# create
@router.post(
    "/create",
    response_model=OrderRow,
    status_code=status.HTTP_201_CREATED,
)
def create_order(order_data: OrderInsert, db: Session = Depends(get_db)):
    order = order_service.create_order(db, order_data)
    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"order cration faild!"
        )
    return order


# update
@router.patch("/update/order_id/{order_id}", response_model=OrderRow)
def update_order(order_id: int, order_data: OrderUpdate, db: Session = Depends(get_db)):
    order = order_service.update_order(db, order_id, order_data)
    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"order cration faild!"
        )
    return order


# delete
@router.delete("/delete/order_id/{order_id}", response_model=OrderDelete)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = order_service.delete_order(db, order_id)
    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"order cration faild!"
        )
    return {"id": order}
