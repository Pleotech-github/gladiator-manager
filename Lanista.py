from Person import *
from Gladiators import *

class Lanista(Person):
    __gladiators = []

    def __init__(self, gladiators: list[Gladiators], exp: int):
        self.__gladiators = gladiators
        self.expierence = exp
