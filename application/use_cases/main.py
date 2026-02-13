from core.domain.main import Fruit, Fruits
from core.inbound_ports.main import FruitService
from core.outbound_ports.main import FruitRepository


class FruitServiceImpl(FruitService):
    def __init__(self, repository: FruitRepository):
        self._repository = repository

    def get_fruits(self) -> Fruits:
        return Fruits(fruits=self._repository.get_all())

    def add_fruit(self, fruit: Fruit) -> Fruit:
        return self._repository.add(fruit)

    def update_fruit(self, old_name: str, new_name: str) -> Fruits:
        return Fruits(fruits=self._repository.update(old_name, new_name))

    def delete_fruit(self, fruit_name: str) -> Fruits:
        return Fruits(fruits=self._repository.delete(fruit_name))
