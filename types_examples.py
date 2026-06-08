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

def barking(pets: List[Pug | LabradorRetriever | Wolfhound ]) -> None:
    for pet in pets:
        pet.bark() 

barking([Pug(), LabradorRetriever(), Sphynx()])
