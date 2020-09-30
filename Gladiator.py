from Person import *
import random


class Gladiator(Person):


    def __init__ \
                    (self,
                     name: str,
                     age: int,
                     weapon_type: str,
                     weapon_dmg: int,
                     toughness: int
                     ):
        Person.__init__(self, name, age)
        self.weapon_type = weapon_type  # the type of weapon the gladiator wields.
        self.weapon_dmg = weapon_dmg  # the amount of damage dealt to a enemy.
        self.health = 100
        self.toughness = toughness  # how much damage the gladiator can withstand.

    def attack(self):
        return self.weapon_dmg * random.random()

    def printinfo(self):
        print("\t", self.__class__.__name__ + " info")
        print("\t\tName: " + str(self.name))
        print("\t\tAge: " + str(self.age))
        print("\t\tStats: ")
        print("\t\t\tWeapon type: " + str(self.weapon_type))
        print("\t\t\tWeapon damage: " + str(self.weapon_dmg))
        print("\t\t\tHealth: " + str(self.health))
        print("\t\t\tToughness: " + str(self.toughness))


