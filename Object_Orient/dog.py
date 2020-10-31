class Dog:
    years = 0
    def dog_years(self):
        return self.years * 7

fido=Dog()
fido.years=3
print(fido.dog_years())

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return "hi, my name is {}".format(self.name)

some_person = Person("Jun")
print(some_person.greeting())
