class Pug:
    def bark(self):
        print("The pug goes arf arf!")

class LabradorRetriever:
    def bark(self):
        print("The labrador retriever goes arf arf!")

class Wolfhound:
    def bark(self):
        print("The wolfhound goes arf arf!")

# pets = [Pug(), LabradorRetriever(), Wolfhound()]

# for pet in pets:
#     pet.bark()

class Sphynx:
    def meow(self):
        print("The sphynx goes meow meow!")

pets = [Pug(), LabradorRetriever(), Sphynx()]

for pet in pets:
    pet.bark()