class Pug:
    def bark(self):
        print("The pug goes arf arf!")

class LabradorRetriever:
    def bark(self):
        print("The labrador retriever goes arf arf!")

class Wolfhound:
    def bark(self):
        print("The wolfhound goes arf arf!")

def make_dogs_bark(pets):
    for pet in pets:
        pet.bark()

# pets = [Pug(), LabradorRetriever(), Wolfhound()]
# make_dogs_bark(pets)

class Sphynx:
    def meow(self):
        print("The sphynx goes meow meow!")

pets = [Pug(), LabradorRetriever(), Sphynx()]
make_dogs_bark(pets)