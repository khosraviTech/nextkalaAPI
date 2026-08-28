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


class TagSchema(BaseModel):
    id: int | None = Field(default=None)
    name: str = Field(default=..., max_length=50)


class TagRow(TagSchema):
    id: int = Field(default=...)  # pyright: ignore[reportIncompatibleVariableOverride]

    # nested relationship objects
    products: list[ProductRow] = []

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

    @field_validator("products", mode="wrap")
    @classmethod
    def _drop_cyclic_products(
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


class TagInsert(TagSchema):
    pass


class TagUpdate(BaseModel):
    id: int = Field(default=...)
    name: str | None = None
    pass


class TagDelete(BaseModel):
    id: int = Field(default=...)
