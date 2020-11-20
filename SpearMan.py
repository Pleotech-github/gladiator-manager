from Gladiator import *


class SpearMan(Gladiator):  # the subclass of the gladiators, which is the type Spear warrior

    def __init__(self, name: str, title: str):
        Gladiator.__init__(self, name, title, "Spear", random.randint(35, 50), random.randint(5, 10))
