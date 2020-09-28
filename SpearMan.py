import random
from Gladiators import *


class SpearMan(Gladiators):  # the subclass of the gladiators, which is the type Spear warrior

    def __init__(self, name: str, age: int):
        Gladiators.__init__(self, name, age, "Spear", random.randint(40, 60), random.randint(50, 100))
