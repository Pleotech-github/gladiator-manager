from Person import *
import random


class Gladiator(Person):
    weapon_type = "Sword"
    # weapon_range: int,
    weapon_dmg = 10
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
        self.health = 100
        self.toughness = toughness  # how much damage the gladiator can withstand.

    def attack(self):
        return self.weapon_dmg * random.uniform(0.3, 1)

    def printinfo(self):
        print("\t", self.__class__.__name__ + " info")
        print("\t\tName: " + str(self.name), str(self.title))
        print("\t\tAge: " + str(self.age))
        print("\t\tStats: ")
        print("\t\t\tWeapon type: " + str(self.weapon_type))
        print("\t\t\tWeapon damage: " + str(self.weapon_dmg))
        print("\t\t\tHealth: " + str(self.health))
        print("\t\t\tToughness: " + str(self.toughness))
