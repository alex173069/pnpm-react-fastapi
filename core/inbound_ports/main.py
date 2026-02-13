from abc import ABC, abstractmethod
from core.domain.main import Fruit, Fruits


class FruitService(ABC):
    @abstractmethod
    def get_fruits(self) -> Fruits:
        pass

    @abstractmethod
    def add_fruit(self, fruit: Fruit) -> Fruit:
        pass

    @abstractmethod
    def update_fruit(self, old_name: str, new_name: str) -> Fruits:
        pass

    @abstractmethod
    def delete_fruit(self, fruit_name: str) -> Fruits:
        pass
