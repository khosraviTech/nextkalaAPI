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
    from . import ProductRow
    from . import CartRow


class CartItemSchema(BaseModel):
    id: int | None = Field(default=None)
    cart_id: int = Field(default=...)
    product_id: int = Field(default=...)
    title: str = Field(default=...)
    price: int = Field(default=...)
    quantity: int = Field(default=...)
    totalItemPrice: int = Field(default=...)


class CartItemRow(CartItemSchema):
    id: int = Field(default=...)  # pyright: ignore[reportIncompatibleVariableOverride]

    # nested relationship objects
    product: ProductRow | None = None
    cart: CartRow | None = None

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

    @field_validator("product", mode="wrap")
    @classmethod
    def _drop_cyclic_product(
        cls, value: Any, handler: Callable[[Any], Any]
    ) -> Any | None:
        try:
            return handler(value)
        except ValidationError as exc:
            if not _is_recursion_validation_error(exc):
                raise
            return None

    @field_validator("cart", mode="wrap")
    @classmethod
    def _drop_cyclic_cart(cls, value: Any, handler: Callable[[Any], Any]) -> Any | None:
        try:
            return handler(value)
        except ValidationError as exc:
            if not _is_recursion_validation_error(exc):
                raise
            return None

    model_config = ConfigDict(from_attributes=True)


class CartItemInsert(CartItemSchema):
    pass


class CartItemUpdate(CartItemSchema):
    pass
