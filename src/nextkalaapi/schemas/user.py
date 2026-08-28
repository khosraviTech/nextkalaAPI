from __future__ import annotations

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
    from . import CartRow
    from . import OrderRow


class Role(str, Enum):
    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"


class UserSchema(BaseModel):
    id: int | None = Field(default=None)
    first_name: str = Field(default=...)
    last_name: str = Field(default=...)
    email: str = Field(default=...)
    password: str = Field(default=...)
    address: str = Field(default=..., max_length=255)
    role: Role | None = Field(default=Role.USER)
    age: int | None = Field(default=None)
    gender: bool | None = Field(default=None)
    image: str | None = Field(default=None)


class UserRow(UserSchema):
    id: int = Field(default=...)  # pyright: ignore[reportIncompatibleVariableOverride]

    # nested relationship objects
    cart: CartRow | None = None
    orders: list[OrderRow] = []

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

    @field_validator("cart", mode="wrap")
    @classmethod
    def _drop_cyclic_cart(cls, value: Any, handler: Callable[[Any], Any]) -> Any | None:
        try:
            return handler(value)
        except ValidationError as exc:
            if not _is_recursion_validation_error(exc):
                raise
            return None

    @field_validator("orders", mode="wrap")
    @classmethod
    def _drop_cyclic_orders(
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


class UserInsert(UserSchema):
    pass


class UserUpdate(BaseModel):
    id: int = Field(default=...)
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    password: str | None = None
    address: str | None = Field(default=None, max_length=255)
    role: Role | None = Field(default=Role.USER)
    age: int | None = None
    gender: bool | None = None
    image: str | None = None


class UserLogin(BaseModel):
    email: str = Field(default=...)
    password: str = Field(default=...)


class UserRegister(UserSchema):
    pass


class UserDelete(BaseModel):
    id: int = Field(default=...)
