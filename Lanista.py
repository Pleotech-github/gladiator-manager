from Person import *
import random


class Lanista(Person):  # Lanista is a gladiator owner and trainer

    def __init__(self, name: str):
        super().__init__(name, random.randint(20, 65))



    def printinfo(self):
        print("\n", self.__class__.__name__ + " info")
        print("Name: " + str(self.name))
        print("Age: " + str(self.age))