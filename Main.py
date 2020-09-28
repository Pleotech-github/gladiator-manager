import Gladiators
import Person
import SpearMan
import random
import SwordMan

for r in range(3):
    miniSpearman = SpearMan.SpearMan(SpearMan.Gladiators.name, SpearMan.Gladiators.age)

    miniSpearman.printinfo()

for r in range(3):
    miniSwordMan = SwordMan.SwordMan(SwordMan.Gladiators.name, SwordMan.Gladiators.age)

    miniSwordMan.printinfo()