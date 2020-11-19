from Person import *
import random


class Gladiator(Person):
    weapon_type = "Sword"
    # weapon_range: int,
    weapon_dmg = 100
    toughness = 50

    def __init__ \
                    (self,
                     name: str,
                     title: str,
                     weapon_type: str,
                     # weapon_range: int,
                     weapon_dmg: int,
                     toughness: int
                     ):
        Person.__init__(self, name, random.randint(17, 27))
        self.title = title
        self.weapon_type = weapon_type  # the type of weapon the gladiator wields.
        # self.weapon_range = weapon_range  # the range of tiles the gladiator can max reach.
        self.weapon_dmg = weapon_dmg  # the amount of damage dealt to a enemy.
        self.health = 60
        self.toughness = toughness  # how much damage the gladiator can withstand.

    def attack(self):
        return self.weapon_dmg * random.uniform(0.9, 1)

    def printinfo(self):
        print("\n\tNAME: \t" + str(self.name), str(self.title))
        print("\tAGE: \t" + str(self.age) + " years")
        print("\tSTATS: \t\t")
        print("\t\tWEAPON TYPE: \t" + str(self.weapon_type))
        print("\t\tWEAPON DAMAGE: \t" + str(self.weapon_dmg))
        print("\t\tHEALTH: \t\t" + str(self.health))
        print("\t\tTOUGHNESS: \t\t" + str(self.toughness))
