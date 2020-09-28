import random
from Lanista import *
import SwordMan
import SpearMan
from typing import List
import numpy as np


class Team:
    name = "Team"
    lanista = Lanista("Marcus", 42)
    gladiators = []

    def __init__(self, name: str, lanista: Lanista, gladiators: List[Gladiator]):
        self.name = name
        self.lanista = lanista
        self.gladiators = gladiators

    def get_random_gladiator(self):
        for i in range(5):
            r = random.randint(0, 20)
            if r <= 10:
                self.gladiators.append(SwordMan)
            else:
                self.gladiators.append(SpearMan)

        print(self.gladiators[num])
