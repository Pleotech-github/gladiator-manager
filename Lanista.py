from Person import *
from Gladiators import *


class Lanista(Person):  # Lanista is a gladiator owner and trainer
    __gladiators = []

    def __init__(self, gladiators: list[Gladiators], exp: int, name, age):
        super().__init__(name, age)
        self.__gladiators = gladiators
        self.experience = exp
