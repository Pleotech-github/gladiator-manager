import random

from Gladiators import *


class SwordMan(Gladiators):
    weapon_type = 'Sword'
    # weapon_range = random.randint(0, 5)
    weapon_dmg = random.randint(40, 60)
    toughness = random.randint(50, 100)

    def __init__(self, weapon):
        self.weapon_type = weapon
        self.weapon_range = random.randint()
