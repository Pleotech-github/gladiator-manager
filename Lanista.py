from Person import *
import Gladiator


class Lanista(Person):  # Lanista is a gladiator owner and trainer

    def __init__(self, name, age):
        super().__init__(name, age)
# self.experience = exp


    def printpimp(self):
        print("\n", self.__class__.__name__ + " info")
        print("Name: " + str(self.name))
        print("Age: " + str(self.age))