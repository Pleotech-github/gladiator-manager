import SpearMan
import SwordMan
import Fighting
import Team as Team
import Lanista
import numpy as np
"""
for r in range(3):
    miniSpearman = SpearMan.SpearMan(SpearMan.Gladiator.name, SpearMan.Gladiator.age)

    miniSpearman.printinfo()

for r in range(3):
    miniSwordMan = SwordMan.SwordMan(SwordMan.Gladiator.name, SwordMan.Gladiator.age)

    miniSwordMan.printinfo()

"""


TeamUno = Team.Team("Team Uno", Lanista.Lanista("Alex", 26))
TeamUno2 = Team.Team("Team Unoaa", Lanista.Lanista("Alex", 26))


fight = Fighting.Fighting()
fight.start_fight(TeamUno,TeamUno2)
#fight.do_fight()

