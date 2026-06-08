from pydantic import BaseModel

class Pug(BaseModel):
    name: str
    age: int
    color: str = "fawn"
    
    def bark(self):
        print(f"The pug {self.name} goes arf arf!")

print("Creating a pug with name 123 and age '14' ...")
new_pug = Pug(name=123, age='14')

# print("Creating a pug with name 'Matty' and age '14' ...")
# new_pug = Pug(name="Matty", age='14')
# print(f"The new pug is named {new_pug.name} which is of type {type(new_pug.name)}")
# print(f"The new pug is aged {new_pug.age} which is of type {type(new_pug.age)}")
# print(f"The new pug has the color {new_pug.color} which is of type {type(new_pug.color)}")
