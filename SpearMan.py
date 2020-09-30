import random
from Gladiator import *


class SpearMan(Gladiator):  # the subclass of the gladiators, which is the type Spear warrior

    def __init__(self, name: str, age: int):
        Gladiator.__init__(self, name, age, "Spear", random.randint(40, 60), random.randint(5, 10))
