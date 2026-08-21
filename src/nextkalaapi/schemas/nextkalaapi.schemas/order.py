from __future__ import annotations

import datetime
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


class OrderSchema(BaseModel):
    id: int | None = Field(default=None)
    user_id: int = Field(default=...)
    subtotal: int = Field(default=...)
    shipping: int = Field(default=...)
    tax: int = Field(default=...)
    total: int = Field(default=...)
    paymentStatus: str | None = Field(default=None, max_length=7)
    orderStatus: str | None = Field(default=None, max_length=10)
    created_at: datetime.datetime | None = Field(default=None)


class OrderRow(OrderSchema):
    id: int = Field(default=...)  # pyright: ignore[reportIncompatibleVariableOverride]

    # nested relationship objects
    items: list[OrderItemRow] = []

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

    @field_validator("items", mode="wrap")
    @classmethod
    def _drop_cyclic_items(
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

    model_config = ConfigDict(from_attributes=True)


class OrderInsert(OrderSchema):
    pass


class OrderUpdate(OrderSchema):
    pass
