class Gladiators:
    def __init__ \
                    (self,
                     weapon_type,
                     weapon_range: int,
                     weapon_dmg: int,
                     toughness: int
                     ):
        self.weapon_type = weapon_type  # the type of weapon the gladiator wields.
        self.weapon_range = weapon_range  # the range of tiles the gladiator can max reach.
        self.weapon_dmg = weapon_dmg  # the amount of damage dealt to a enemy.
        self.toughness = toughness  # how much damage the gladiator can withstand.


class Fighter(Gladiators):  # the subclass of the gladiators, which is the type fighter
    pass


class SpearMan(Gladiators):
    pass


class StoneSlinger(Gladiators):
    pass
