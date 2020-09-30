import random
from Lanista import *
import SwordMan
import SpearMan
#from typing import List
#import numpy as np


class Team:
    name = "Team"
    lanista = Lanista("Marcus", 42)
    gladiators = []

    def __init__(self, name: str, lanista: Lanista, gladiators: [Gladiator]):
        self.name = name
        self.lanista = lanista
        self.gladiators = gladiators

    for i in range(2):
        gladiators.append(SwordMan.SwordMan(SwordMan.Gladiator.name, SwordMan.Gladiator.age).printinfo())


    for i in range(2):
        gladiators.append(SpearMan.SpearMan(SpearMan.Gladiator.name, SpearMan.Gladiator.age).printinfo())



    """
    @classmethod
    def get_random_gladiator(cls):
        for i in range(5):
            r = random.randint(0, 20)
            if r <= 10:
                cls.gladiators.append(SwordMan)
            else:
                cls.gladiators.append(SpearMan)
    


    def printteam(self):
        print("\n", self.__class__.__name__ + " info")
        print("Name: " + str(self.name))
        print("Lanista: " + str(self.lanista))
        print(self.gladiators)

    def print_fighter(self, num: int):

        print(self.gladiators[num])
    """