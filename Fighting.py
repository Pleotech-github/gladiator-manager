import Team
import random


class Fighting:
    team1 = ""
    team2 = ""
    gladiator1 = "Gladiator_1"
    gladiator2 = "Gladiator_2"

    def do_fight(self):

        if random.randint(0,2) == 1:
            dmg = self.gladiator2.attack()
            print(self.gladiator2.name + " did " + str(dmg) + " damage.")
            self.gladiator1.toughness -= dmg
        else:
            dmg = self.gladiator1.attack()
            print(self.gladiator1.name + " did " + str(dmg) + " damage.")
            self.gladiator1.toughness -= dmg

        if self.gladiator1.toughness <= 0:
            print(self.gladiator2.name + " from the team " + self.team2.name + " killed " + self.gladiator1.name)
        elif self.gladiator2.toughness <= 0:
            print(self.gladiator1.name + " from the team " + self.team1.name + " killed " + self.gladiator2.name)
        else:
            print("No one died")
            print("Remaining health:\n\t" + self.gladiator1.name + "\n\t\t" + str(self.gladiator1.toughness))
            print("Remaining health:\n\t" + self.gladiator2.name + "\n\t\t" + str(self.gladiator2.toughness))

    def start_fight(self, t1: Team, t2: Team):
        self.gladiator1 = t1.gladiators[random.randint(0, 3)]
        self.gladiator2 = t2.gladiators[random.randint(0, 3)]
        self.team1 = t1
        self.team2 = t2

        while self.gladiator1.toughness > 0 and self.gladiator2.toughness > 0:
            print("Press any key to fight")
            input()
            self.do_fight()
