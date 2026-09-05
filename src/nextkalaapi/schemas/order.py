from __future__ import annotations

import datetime
from enum import Enum
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
    from . import OrderItemRow
    from . import UserRow


class OrderStatus(str, Enum):
    processing = "processing"
    cancelled = "cancelled"
    shipped = "shipped"
    delivered = "delivered"


class PaymentStatus(str, Enum):
    pending = "pending"
    paid = "paid"
    failed = "failed"


class OrderSchema(BaseModel):
    # id: int | None = Field(default=None)
    subtotal: int = Field(default=...)
    shipping: int = Field(default=...)
    tax: int = Field(default=...)
    total: int = Field(default=...)
    paymentStatus: str | None = Field(default=None, max_length=7)
    orderStatus: str | None = Field(default=None, max_length=10)
    created_at: datetime.datetime | None = Field(default=None)
    user_id: int = Field(default=...)


class OrderRow(OrderSchema):
    id: int = Field(default=...)  # pyright: ignore[reportIncompatibleVariableOverride]

    # nested relationship objects
    order_items: list[OrderItemRow] = []
    user: UserRow | None = None

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

    @field_validator("user", mode="wrap")
    @classmethod
    def _drop_cyclic_user(cls, value: Any, handler: Callable[[Any], Any]) -> Any | None:
        try:
            return handler(value)
        except ValidationError as exc:
            if not _is_recursion_validation_error(exc):
                raise
            return None

    model_config = ConfigDict(from_attributes=True)


class OrderInsert(OrderSchema):
    pass


class OrderUpdate(BaseModel):
    id: int = Field(default=...)
    subtotal: int | None = None
    shipping: int | None = None
    tax: int | None = None
    total: int | None = None
    paymentStatus: PaymentStatus | None = Field(default=PaymentStatus.pending)
    orderStatus: OrderStatus | None = Field(default=OrderStatus.processing)
    created_at: datetime.datetime | None = Field(default=None)
    user_id: int | None = Field(default=...)


class OrderDelete(BaseModel):
    id: int = Field(default=...)
