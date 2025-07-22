
class Person:
    def __init__(self,name, age):
          self.name = name
          self.age = age
    def show(self):
         print(f"Name: {self.name} , Age: {self.age}")


person = Person("Alice",25)

person.show()