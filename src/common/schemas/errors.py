from dataclasses import dataclass
from typing import (
    Generic,
    TypeVar,
)

from pydantic.generics import GenericModel

TData = TypeVar("TData")


@dataclass(frozen=True)
class ErrorMessage(GenericModel, Generic[TData]):
    message: str
