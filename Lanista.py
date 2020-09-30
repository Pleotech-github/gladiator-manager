from Person import *
import random

class Lanista(Person):  # Lanista is a gladiator owner and trainer

    def __init__(self, name):
        super().__init__(name, random.randint(16, 65))

    def printinfo(self):
         print("\tLanista name: " + self.name)
         print("\tLanista age: " + str(self.age))

