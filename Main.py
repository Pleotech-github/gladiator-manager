import Gladiators
import Person
import SpearMan
import random

miniGladiator = Gladiators.Gladiators(Person.Person.name,
                                      Person.Person.age,
                                      Gladiators.Gladiators.weapon_type,
                                      Gladiators.Gladiators.weapon_dmg,
                                      Gladiators.Gladiators.toughness
                                      )
miniGladiator.printinfo()

miniSpearman1 = SpearMan.Gladiators(SpearMan.Gladiators.name, SpearMan.Gladiators.age, SpearMan.SpearMan.weapon_type,
                                    random.randint(40, 60),
                                    SpearMan.SpearMan.toughness)
miniSpearman2 = SpearMan.Gladiators(SpearMan.Gladiators.name, SpearMan.Gladiators.age, SpearMan.SpearMan.weapon_type,
                                    SpearMan.SpearMan.randomDamage(SpearMan.SpearMan.weapon_dmg),
                                    SpearMan.SpearMan.toughness)
miniSpearman3 = SpearMan.Gladiators(SpearMan.Gladiators.name, SpearMan.Gladiators.age, SpearMan.SpearMan.weapon_type,
                                    SpearMan.SpearMan.randomDamage(SpearMan.SpearMan.weapon_dmg),
                                    SpearMan.SpearMan.toughness)

miniSpearman1.printinfo()
miniSpearman2.printinfo()
miniSpearman3.printinfo()
