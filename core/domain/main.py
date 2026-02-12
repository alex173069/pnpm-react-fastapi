from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from typing import List

class Fruit(BaseModel):
    name: str

class Fruits(BaseModel):
    fruits: List[Fruit]

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:5174",  # Vite dev server
    "http://localhost:3000"   # In case frontend runs on different port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

memory_db = {"fruits": []}

@app.get("/fruits", response_model=Fruits)
def get_fruits():
    return Fruits(fruits=memory_db["fruits"])

@app.post("/fruits", response_model=Fruit)
def add_fruit(fruit: Fruit):
    memory_db["fruits"].append(fruit)
    return fruit

@app.put("/fruits", response_model=Fruits)
def update_fruit(old_name: str, new_name: str):
    for fruit in memory_db["fruits"]:
        if fruit.name == old_name:
            fruit.name = new_name
            break
    return Fruits(fruits=memory_db["fruits"])

@app.delete("/fruits", response_model=Fruits)
def delete_fruit(fruit_name: str): # FastAPI looks for 'fruit_name' in the URL query string
    memory_db["fruits"] = [fruit for fruit in memory_db["fruits"] if fruit.name != fruit_name]
    return Fruits(fruits=memory_db["fruits"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)