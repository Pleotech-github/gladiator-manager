import Team
import random


class Fighting:
    team1 = ""
    team2 = ""
    gladiator1 = "Gladiator_1"
    gladiator2 = "Gladiator_2"

    def do_fight(self):

        if random.randint(0,2) == 1:
            dmg = self.gladiator2.attack()-self.gladiator1.toughness
            print(self.gladiator2.name + " attacked and did " + str(dmg) + " damage.")
            self.gladiator1.health -= dmg
        else:
            dmg = self.gladiator1.attack()-self.gladiator2.toughness
            print(self.gladiator1.name + " attacked and did " + str(dmg) + " damage.")
            self.gladiator2.health -= dmg

        if self.gladiator1.health <= 0:
            print(self.gladiator2.name + " from " + self.team2.name + " killed " + self.gladiator1.name + " from  " + self.team1.name)
        elif self.gladiator2.health <= 0:
            print(self.gladiator1.name + " from  " + self.team1.name + " killed " + self.gladiator2.name + " from " + self.team2.name)
        else:
            print("Remaining health:\n\t" + self.gladiator1.name + ": " + str(self.gladiator1.health))
            print("Remaining health:\n\t" + self.gladiator2.name + ": " + str(self.gladiator2.health))
            print("No one died")
            print("\n\t\t******")

    def start_fight(self, t1: Team, t2: Team):
        self.gladiator1 = t1.gladiators[random.randint(0, len(t1.gladiators)-1)]
        self.gladiator2 = t2.gladiators[random.randint(0, len(t2.gladiators)-1)]
        self.team1 = t1
        self.team2 = t2

        print(self.gladiator1.name + " from " + t1.name + " is fighting " + self.gladiator2.name + " from " + t2.name)

        while self.gladiator1.toughness > 0 and self.gladiator2.toughness > 0:

            print("\n\tPress any key to fight")
            input()
            self.do_fight()
