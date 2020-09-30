class Person:  # a person who can be either Lanista or gladiator
    name = "Maximus"
    age = "20"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def printinfo(self):
        print("\n", self.__class__.__name__ + " info")
        print("Name: " + self.name)
        print("Age: " + str(self.age))

