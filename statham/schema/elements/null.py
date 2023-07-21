from typing import Any, List

from statham.schema.elements.base import Element
from statham.schema.constants import Maybe, NotPassed
from statham.schema.validation import InstanceOf


class Null(Element[None]):
    """JSON Schema ``"null"`` element."""

    def __init__(
        self,
        *,
        default: Maybe[None] = NotPassed(),
        const: Maybe[Any] = NotPassed(),
        enum: Maybe[List[Any]] = NotPassed(),
        description: Maybe[str] = NotPassed(),
    ):
        self.default = default
        self.const = const
        self.enum = enum
        self.description = description

    @property
    def annotation(self) -> str:
        return "None"

    @property
    def type_validator(self):
        return InstanceOf(type(None))
