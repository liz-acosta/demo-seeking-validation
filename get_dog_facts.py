import requests
import unittest
from unittest.mock import patch
from pydantic import BaseModel, Field

DOG_API_BASE_URL = "https://dogapi.dog/api/v2/"


class DogBreedInfo(BaseModel):
    name: str
    description: str
    lifespan: int
    weight: int
    breed_group: str

    def generate_dog_info_final(self) -> str:
        dog_breed_info_final = f"Dog breed info for the {self.name}: {self.description} {self.name}s are part of the {self.breed_group} and can weigh up to {self.weight}kg and live up to {self.lifespan} years."
        return dog_breed_info_final


def get_breed_id(dog_breed_input=str) -> list[str]:

    dog_breed_info_url = f"{DOG_API_BASE_URL}breeds"

    dog_breeds_response = requests.get(dog_breed_info_url).json()

    breed_id = [
        dog_breed["id"]
        for dog_breed in dog_breeds_response["data"]
        if dog_breed["attributes"]["name"].lower() == dog_breed_input.lower()
    ]

    return breed_id


def get_dog_breed_info(dog_breed_input=str) -> dict:

    dog_breed_id = get_breed_id(dog_breed_input)[0]

    dog_breed_info_url = f"{DOG_API_BASE_URL}breeds/{dog_breed_id}"
    dog_breed_info_response = requests.get(dog_breed_info_url).json()

    dog_breed_info = dog_breed_info_response["data"]["attributes"]
    name = dog_breed_info["name"]
    description = dog_breed_info["description"]
    lifespan = dog_breed_info["life"]["max"]
    weight = dog_breed_info["male_weight"]["max"]

    breed_group_id = dog_breed_info_response["data"]["relationships"]["group"]["data"][
        "id"
    ]

    dog_breed_info = {
        "name": name,
        "description": description,
        "lifespan": lifespan,
        "weight": weight,
        "breed_group_id": breed_group_id,
    }

    return dog_breed_info


def get_breed_group(breed_group_id=str) -> str:
    dog_breed_group_url = f"{DOG_API_BASE_URL}groups/{breed_group_id}"

    dog_breed_group_response = requests.get(dog_breed_group_url).json()
    dog_breed_group = dog_breed_group_response["data"]["attributes"]["name"]

    return dog_breed_group


def generate_dog_facts(dog_breed_input=str) -> DogBreedInfo:

    dog_info = get_dog_breed_info(dog_breed_input)

    breed_group = get_breed_group(dog_info["breed_group_id"])

    dog_breed_facts = DogBreedInfo(
        name=dog_info["name"],
        description=dog_info["description"],
        lifespan=dog_info["lifespan"],
        weight=dog_info["weight"],
        breed_group=breed_group,
    )

    return dog_breed_facts


def main():
    print("Which dog breed do you want facts for?: ")
    dog_breed_input = input()
    dog_facts = generate_dog_facts(dog_breed_input)
    dog_facts_final = dog_facts.generate_dog_info_final()
    return dog_facts_final


if __name__ == "__main__":
    output = main()
    print(output)
