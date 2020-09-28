import random
from Person import *
from Gladiators import *


class SpearMan(Gladiators):  # the subclass of the gladiators, which is the type Spear warrior
    weapon_type = 'humongous Spear'
    # weapon_range = random.randint(3, 10)
    weapon_dmg = int()
    toughness = random.randint(50, 100)

    def randomDamage(self):
        self.weapon_dmg = random.randint(40, 60)
