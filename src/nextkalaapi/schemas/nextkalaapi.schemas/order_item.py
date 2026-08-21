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
    from . import OrderRow


class OrderItemSchema(BaseModel):
    id: int | None = Field(default=None)
    title: str = Field(default=..., max_length=50)
    price: int = Field(default=...)
    quantity: int = Field(default=...)
    total_item_price: int = Field(default=...)
    order_id: int = Field(default=...)
    product_id: int = Field(default=...)


class OrderItemRow(OrderItemSchema):
    id: int = Field(default=...)  # pyright: ignore[reportIncompatibleVariableOverride]

    # nested relationship objects
    product: ProductRow | None = None
    order: OrderRow | None = None

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

    @field_validator("order", mode="wrap")
    @classmethod
    def _drop_cyclic_order(
        cls, value: Any, handler: Callable[[Any], Any]
    ) -> Any | None:
        try:
            return handler(value)
        except ValidationError as exc:
            if not _is_recursion_validation_error(exc):
                raise
            return None

    model_config = ConfigDict(from_attributes=True)


class OrderItemInsert(OrderItemSchema):
    pass


class OrderItemUpdate(OrderItemSchema):
    pass
