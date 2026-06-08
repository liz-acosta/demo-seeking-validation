from typing import List

class Pug:
    def __init__(self, name: str) -> None:
        self.name: str = name
    
    def bark(self) -> None:
        print(f"The pug {self.name} goes arf arf!")

class LabradorRetriever:
    def bark(self) -> None:
        print("The labrador retriever goes arf arf!")

class Wolfhound:
    def bark(self) -> None:
        print("The wolfhound goes arf arf!")

class Sphynx:
    def meow(self) -> None:
        print("The sphynx goes meow meow!")

def make_dogs_bark(pets: List[Pug | LabradorRetriever | Wolfhound ]) -> None:
    for pet in pets:
        pet.bark() 

make_dogs_bark([Pug(), LabradorRetriever(), Sphynx()])
