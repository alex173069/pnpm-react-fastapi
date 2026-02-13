from core.domain.main import Fruit
from core.outbound_ports.main import FruitRepository


class InMemoryFruitRepository(FruitRepository):
    def __init__(self):
        self._fruits: list[Fruit] = []

    def get_all(self) -> list[Fruit]:
        return self._fruits.copy()

    def add(self, fruit: Fruit) -> Fruit:
        self._fruits.append(fruit)
        return fruit

    def update(self, old_name: str, new_name: str) -> list[Fruit]:
        for fruit in self._fruits:
            if fruit.name == old_name:
                fruit.name = new_name
                break
        return self._fruits.copy()

    def delete(self, fruit_name: str) -> list[Fruit]:
        self._fruits = [f for f in self._fruits if f.name != fruit_name]
        return self._fruits.copy()
