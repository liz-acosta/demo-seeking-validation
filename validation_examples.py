from typing import List

class Pug:
    def __init__(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name.strip():
            raise ValueError("name cannot be empty")

        self.name = name

    def bark(self) -> None:
        print(f"The pug {self.name} goes arf arf!")

class LabradorRetriever:
    def __init__(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name.strip():
            raise ValueError("name cannot be empty")

        self.name = name

    def bark(self) -> None:
        print(f"The labrador retriever {self.name} goes arf arf!")

class Wolfhound:
    def __init__(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name.strip():
            raise ValueError("name cannot be empty")

        self.name = name

    def bark(self) -> None:
        print(f"The wolfhound {self.name} goes arf arf!")

class Sphynx:
    def __init__(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name.strip():
            raise ValueError("name cannot be empty")

        self.name = name

    def meow(self) -> None:
        print(f"The sphynx {self.name} goes meow meow!")

def make_dogs_bark_safely(pets: List[Pug | LabradorRetriever | Wolfhound ]) -> None:
    """Manual validation in the function"""
    for pet in pets:
        if not hasattr(pet, 'bark') or not callable(getattr(pet, 'bark')):
            raise TypeError(f"Invalid dog type: {type(pet).__name__}")
        pet.bark()

# Now this fails immediately with a clear message:
pets = [Pug(), Sphynx()]
make_dogs_bark_safely(pets)
