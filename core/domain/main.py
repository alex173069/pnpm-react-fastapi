from pydantic import BaseModel


class Fruit(BaseModel):
    name: str


class Fruits(BaseModel):
    fruits: list[Fruit]
