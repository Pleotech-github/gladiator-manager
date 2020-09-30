import random
from Lanista import *
import SwordMan
import SpearMan


class Team:
    names = ["Tom", "Sam", "Bob", "Loi", "Tommy", "Sammy", "Laban"]

    def __init__(self, name: str, lanista: Lanista):
        self.name = name
        self.lanista = lanista
        self.gladiators = []

        for i in range(2):
            self.gladiators.append(SwordMan.SwordMan(self.names[random.randint(0, len(self.names)-1)], 43))

        for i in range(2):
            self.gladiators.append(SpearMan.SpearMan(self.names[random.randint(0, len(self.names)-1)], 43))

    def print_team(self):
        print(self.__class__.__name__ + " info")
        print("\tName: " + str(self.name))
        self.lanista.printinfo()
        print("\nGladiators:")
        print("\tNumber of gladiator: " + str(len(self.gladiators)))
        for glad in self.gladiators:
            glad.printinfo()
        print("\n----------------------------------\n")

    def print_fighter(self, num: int):
        self.gladiators[num].printinfo()
