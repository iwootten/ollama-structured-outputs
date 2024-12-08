from typing import List
from ollama import chat
from pydantic import BaseModel

class City(BaseModel):
    name: str
    country: str

class Cities(BaseModel):
    cities: List[City]

response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "List 5 cities from around the world and their countries",
        }
    ],
    format=Cities.model_json_schema(),
)

city_list = Cities.model_validate_json(response.message.content)

print(city_list)