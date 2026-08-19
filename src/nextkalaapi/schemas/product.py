from pydantic import BaseModel

from pydantic import BaseModel


class Dimensions(BaseModel):
    width: float
    height: float
    depth: float


class Review(BaseModel):
    rating: float
    comment: str
    date: str
    reviewerName: str
    reviewerEmail: str


class Meta(BaseModel):
    createdAt: str
    updatedAt: str
    barcode: str
    qrCode: str


class Product(BaseModel):
    id: int
    title: str
    description: str
    category: str | None = None
    price: float
    discountPercentage: float | None = None
    rating: float | None = None
    stock: int | None = None
    tags: list[str] | None = None
    brand: str | None = None
    sku: str | None = None
    weight: float | None = None
    dimensions: Dimensions | None = None
    warrantyInformation: str | None = None
    shippingInformation: str | None = None
    availabilityStatus: str | None = None
    reviews: list[Review] | None = None
    returnPolicy: str | None = None
    minimumOrderQuantity: int | None = None
    meta: Meta | None = None
    images: list[str] | None = None
    thumbnail: str | None = None
