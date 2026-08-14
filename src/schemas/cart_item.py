
from pydantic import BaseModel


class CartItem(BaseModel):
    id: int
    title: str
    image: list[str]
    price: int
    quantity: int
    totalItemPrice: int