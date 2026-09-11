from fastapi import FastAPI
from scalar_fastapi import add_scalar_reference

from nextkalaapi.routers import carts, orders, products, users

app = FastAPI()
add_scalar_reference(app)

app.include_router(users.router, prefix="/users", tags=["user"])
app.include_router(orders.router, prefix="/orders", tags=["order"])
app.include_router(products.router, prefix="/products", tags=["product"])
app.include_router(carts.router, prefix="/carts", tags=["cart"])



@app.get("/")
def read_root():
    return {"Hello": "nextkala API"}
