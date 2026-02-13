from abc import ABC, abstractmethod
from core.domain.main import Fruit


class FruitRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Fruit]:
        pass

    @abstractmethod
    def add(self, fruit: Fruit) -> Fruit:
        pass

    @abstractmethod
    def update(self, old_name: str, new_name: str) -> list[Fruit]:
        pass

    @abstractmethod
    def delete(self, fruit_name: str) -> list[Fruit]:
        pass
