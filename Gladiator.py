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
                     age: int,
                     weapon_type: str,
                     # weapon_range: int,
                     weapon_dmg: int,
                     toughness: int
                     ):
        Person.__init__(self, name, age)
        self.weapon_type = weapon_type  # the type of weapon the gladiator wields.
        # self.weapon_range = weapon_range  # the range of tiles the gladiator can max reach.
        self.weapon_dmg = weapon_dmg  # the amount of damage dealt to a enemy.
        self.toughness = toughness  # how much damage the gladiator can withstand.

    def attack(self):
        return self.weapon_dmg * random.random()

    def printinfo(self):
        print("\n", self.__class__.__name__ + " info")
        print("Name: " + str(self.name))
        print("Age: " + str(self.age))
        print("Stats: " + str(self.weapon_type), ", Weapon damage: " + str(self.weapon_dmg),
              ", Toughness: " + str(self.toughness))
