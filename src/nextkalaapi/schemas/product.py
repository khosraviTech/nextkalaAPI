from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    model_validator,
    field_validator,
    ValidationError,
)

from sqlalchemy.exc import MissingGreenlet


def _is_recursion_validation_error(exc: ValidationError) -> bool:
    errs = exc.errors()
    return len(errs) == 1 and errs[0]["type"] == "recursion_loop"


if TYPE_CHECKING:
    from . import CartItemRow
    from . import OrderItemRow
    from . import TagRow


class ProductSchema(BaseModel):
    # id: int | None = Field(default=None)
    title: str = Field(default=..., max_length=100)
    description: str = Field(default=..., max_length=300)
    category: str = Field(default=..., max_length=50)
    price: float = Field(default=...)
    brand: str = Field(default=...)
    images: list[Any] = Field(default=...)


class ProductRow(ProductSchema):
    id: int = Field(default=...)  # pyright: ignore[reportIncompatibleVariableOverride]

    # nested relationship objects
    cart_items: list[CartItemRow] = []
    order_items: list[OrderItemRow] = []
    tags: list[TagRow] = []

    @model_validator(mode="before")
    @classmethod
    def _extract_attrs(cls, obj: Any) -> dict[str, Any]:
        if isinstance(obj, dict):
            return obj  # pyright: ignore[reportUnknownVariableType]
        data: dict[str, Any] = {}
        for name, _ in cls.model_fields.items():
            try:
                data[name] = getattr(obj, name)
            except MissingGreenlet:
                # relationship wasn’t loaded — leave at the schema’s default
                continue
            except Exception:
                # any other getattr‑error: skip too
                continue
        return data

    @field_validator("cart_items", mode="wrap")
    @classmethod
    def _drop_cyclic_cart_items(
        cls, value: Any, handler: Callable[[Any], Any]
    ) -> Any | None:
        try:
            return handler(value)
        except ValidationError as exc:
            if not _is_recursion_validation_error(exc):
                raise
            pruned: list[Any] = []
            for item in value or []:  # pyright: ignore[reportUnknownVariableType]
                try:
                    pruned.extend(handler([item]))
                except ValidationError:
                    continue
            return pruned

    @field_validator("order_items", mode="wrap")
    @classmethod
    def _drop_cyclic_order_items(
        cls, value: Any, handler: Callable[[Any], Any]
    ) -> Any | None:
        try:
            return handler(value)
        except ValidationError as exc:
            if not _is_recursion_validation_error(exc):
                raise
            pruned: list[Any] = []
            for item in value or []:  # pyright: ignore[reportUnknownVariableType]
                try:
                    pruned.extend(handler([item]))
                except ValidationError:
                    continue
            return pruned

    @field_validator("tags", mode="wrap")
    @classmethod
    def _drop_cyclic_tags(cls, value: Any, handler: Callable[[Any], Any]) -> Any | None:
        try:
            return handler(value)
        except ValidationError as exc:
            if not _is_recursion_validation_error(exc):
                raise
            pruned: list[Any] = []
            for item in value or []:  # pyright: ignore[reportUnknownVariableType]
                try:
                    pruned.extend(handler([item]))
                except ValidationError:
                    continue
            return pruned

    model_config = ConfigDict(from_attributes=True)


class ProductInsert(ProductSchema):
    pass


class ProductUpdate(BaseModel):
    id: int = Field(default=...)
    title: str | None = None
    description: str | None = None
    category: str | None = None
    price: float | None = None
    brand: str | None = None
    images: list[Any] | None = None


class ProductDelete(BaseModel):
    id: int = Field(default=...)


class ProductSearch(BaseModel):
    title: str | None = None
    category: str | None = None
    brand: str | None = None
    min_price: float | None = None
    max_price: float | None = None


class ProductFilter(BaseModel):
    category: str | None = None
    brand: str | None = None
    min_price: float | None = None
    max_price: float | None = None
