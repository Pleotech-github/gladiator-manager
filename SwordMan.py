import random
from Gladiator import *


class SwordMan(Gladiator):  # the subclass of the gladiators, which is the type Spear warrior

    def __init__(self, name: str, age: int):
        Gladiator.__init__(self, name, age, "Sword", random.randint(50, 70), random.randint(50, 120))
