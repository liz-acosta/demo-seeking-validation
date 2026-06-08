from typing import List

class Pug:
    def bark(self) -> None:
        print("The pug goes arf arf!")

class LabradorRetriever:
    def bark(self) -> None:
        print("The labrador retriever goes arf arf!")

class Wolfhound:
    def bark(self) -> None:
        print("The wolfhound goes arf arf!")

class Sphynx:
    def meow(self) -> None:
        print("The sphynx goes meow meow!")

def make_dogs_bark_safely(pets: List[Pug | LabradorRetriever | Wolfhound ]) -> None:
    """Manual validation in the function"""
    for pet in pets:
        if not hasattr(pet, 'bark') or not callable(getattr(pet, 'bark')):
            raise TypeError(f"Invalid dog type: {type(pet).__name__}")
        pet.bark()

# Now this fails immediately with a clear message:
pets = [Pug(), Sphynx()]
make_dogs_bark_safely(pets)
