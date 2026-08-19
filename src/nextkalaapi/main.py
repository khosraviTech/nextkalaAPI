from fastapi import FastAPI

from nextkalaapi.routers import orders, products, users

app = FastAPI()

app.include_router(users.router,prefix='/users',tags=["user"])
app.include_router(orders.router ,prefix='/orders',tags=["order"])
app.include_router(products.router ,prefix='/products',tags=["product"])

@app.get("/")
def read_root():
    return {"Hello": "World"}


