import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from infra.outbound_adapters.database.main import InMemoryFruitRepository
from application.use_cases.main import FruitServiceImpl
from infra.inbound_adapters.api.main import create_fruit_router


def create_app() -> FastAPI:
    repository = InMemoryFruitRepository()
    service = FruitServiceImpl(repository)
    app = create_fruit_router(service)

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
