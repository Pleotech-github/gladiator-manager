import random
from Lanista import *
import SwordMan
import SpearMan
from collections import deque
#from typing import List
#import numpy as np


class Team:
    names = ["Atticus", "Augustus", "Aurelius", "Claudius", "Julius", "Hadrian", "Magnus", "Marcellus",
             "Maximus", "Octavius", "Judas", "Jesus", "Romanus", "Pseudolus", "Alexandru", "Auxilium", "Augustinus",
             "Felicius"]

    titles = ["the Crooked", "the Bonemachine", "the Vicious", "Iron Grip", "Tough Stuff", "the Impure", "the Screamer",
              "the Diseased", "the Deceased", "Skullmantle", "Ragestare", "Bonecrusher", "Ironbrow", "the Agonizer",
              "the Chosen", "Potter", "Death Mane", "the Feral", "the Drake", "Dragonborn", "Ironfist", "the Betrayer",
              "the Glutenous"]

    lan_names = ["HEJEJEJEJE"]


    def __init__(self, name: str):
        self.name = name
        self.lan_names = "Bob"
            #Lanista.Lanista([random.randint(0, len(self.names)-1)])
        self.gladiators = []

        for i in range(2):
            randomName = random.randint(0, len(self.names) - 1)
            randomTitle = random.randint(0, len(self.titles) - 1)
            self.gladiators.append(SwordMan.SwordMan(self.names[randomName],
                                   (self.titles[randomTitle])))



        for i in range(2):
            randomName = random.randint(0, len(self.names) - 1)
            randomTitle = random.randint(0, len(self.titles) - 1)
            self.gladiators.append(SpearMan.SpearMan(self.names[randomName],
                                                     (self.titles[randomTitle])))


    def printteam(self):
        print("\n", self.__class__.__name__ + " info")
        print("Name: " + str(self.name))
     #   self.lanista.printinfo()
        print("Gladiators:")
        print("Number of gladiators: " + str(len(self.gladiators)))
        self.gladiators.sort(key=lambda x: x.name)
        for gladiators in self.gladiators:
            gladiators.printinfo()
        print("------------------------------------------------")


    def print_fighter(self, num: int):
        self.gladiators[num].printinfo()
