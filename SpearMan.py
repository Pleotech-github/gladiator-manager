import random
from Gladiators import *


class SpearMan(Gladiators):  # the subclass of the gladiators, which is the type Spear warrior

    def __init__(self, name: str, age: int):
        Gladiators.__init__(self, name, age, "Spear", random.randint(40, 60), random.randint(50, 100))

    """       
 weapon_type = 'humongous Spear'
     weapon_range = random.randint(3, 10)
    weapon_dmg = int()
    self.weapon_dmg = random.randint(40, 60)
    toughness = random.randint(50, 100)
    
 """
