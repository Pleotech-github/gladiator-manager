import random
from Lanista import *
import SwordMan
import SpearMan


class Team:
    name = "Team"
    gladiators = []
    names = ["Tom", "Sam", "Bob", "Loi", "Tommy", "Sammy", "Laban"]

    def __init__(self, name: str, lanista: Lanista):
        self.name = name
        self.lanista = lanista

        for i in range(2):
            self.gladiators.append(SwordMan.SwordMan(self.names[random.randint(0, len(self.names)-1)], 43))

        for i in range(2):
            self.gladiators.append(SpearMan.SpearMan(self.names[random.randint(0, len(self.names)-1)], 43))

    def print_team(self):
        print("\n", self.__class__.__name__ + " info")
        print("Name: " + str(self.name))
        print("Lanista: " + str(self.lanista.printinfo()))
        for glad in self.gladiators:
            glad.printinfo()

    def print_fighter(self, num: int):
        self.gladiators[num].printinfo()
