
from Gladiator import *


class SwordMan(Gladiator):  # the subclass of the gladiators, which is the type Spear warrior

    def __init__(self, name: str, title: str):
        Gladiator.__init__(self, name, title, "Sword", random.randint(30, 40), random.randint(5, 12))




