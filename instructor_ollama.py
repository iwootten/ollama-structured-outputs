from typing import List
from openai import OpenAI
from pydantic import BaseModel
import instructor


class City(BaseModel):
    name: str
    country: str

class Cities(BaseModel):
    cities: List[City]

# enables `response_model` in create call
client = instructor.from_openai(
    OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama",  # required, but unused
    ),
    mode=instructor.Mode.JSON,
)

city_list = client.chat.completions.create(
    model="llama2",
    messages=[
        {
            "role": "user",
            "content": "List 5 cities from around the world and their countries",
        }
    ],
    response_model=Cities,
)

print(city_list)