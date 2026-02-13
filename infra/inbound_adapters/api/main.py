from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from core.domain.main import Fruit, Fruits
from core.inbound_ports.main import FruitService


def create_fruit_router(service: FruitService) -> FastAPI:
    app = FastAPI()

    origins = [
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/fruits", response_model=Fruits)
    def get_fruits():
        return service.get_fruits()

    @app.post("/fruits", response_model=Fruit)
    def add_fruit(fruit: Fruit):
        return service.add_fruit(fruit)

    @app.put("/fruits", response_model=Fruits)
    def update_fruit(old_name: str, new_name: str):
        return service.update_fruit(old_name, new_name)

    @app.delete("/fruits", response_model=Fruits)
    def delete_fruit(fruit_name: str):
        return service.delete_fruit(fruit_name)

    return app
