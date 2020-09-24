class Gladiators:
    def __init__ \
                    (self,
                     weapon_type,
                     weapon_range: int,
                     weapon_dmg: int,
                     max_hp: int,

                     ):
        self.weapon_type = weapon_type  # the type of weapon the gladiator wields.
        self.weapon_range = weapon_range  # the range of title the gladiator can max reach.
        self.weapon_dmg = weapon_dmg  # the amount of damage dealt to a enemy.
        self.max_hp = max_hp  # how much damage it can withstand.


class Fighter(Gladiators):  # the subclass of the gladiators, which is the type fighter
    pass


class SpearMan(Gladiators):
    pass


class StoneSlinger(Gladiators):
    pass


gla_1 = Fighter('sword', 1, 3, 3)
gla_2 = SpearMan('spear', 2, 3, 3)
gla_3 = StoneSlinger('Sling', 3, 2, 2)
print(gla_1.weapon_type)
print(gla_2.weapon_type)
