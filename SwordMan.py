import random
from Gladiators import *


class SwordMan(Gladiators):  # the subclass of the gladiators, which is the type Spear warrior

    def __init__(self, name: str, age: int):
        Gladiators.__init__(self, name, age, "Sword", random.randint(50, 70), random.randint(50, 120))
