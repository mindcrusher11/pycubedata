from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T")


class DBOps(ABC):
    @abstractmethod
    def read(self, data):
        pass

    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def update(self, data):
        pass

    @abstractmethod
    def delete(self, data):
        pass
