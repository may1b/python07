from abc import ABC, abstractmethod
from typing import Optional


class HealCapability(ABC):

    @abstractmethod
    def heal(self, target: Optional[str] = None) -> str:
        raise NotImplementedError


class TransformCapability(ABC):

    def __init__(self) -> None:
        self._transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def revert(self) -> str:
        raise NotImplementedError


__all__: list[str] = [
    "HealCapability",
    "TransformCapability",
]
