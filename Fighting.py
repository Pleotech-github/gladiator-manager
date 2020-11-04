import Team
import random
import array as arr


class Fighting:
    team1 = ""
    team2 = ""

    gladiator1 = "Gladiator_1"
    gladiator2 = "Gladiator_2"

    round_num = 1

    def do_fight(self):

        if random.randint(0, 2) == 1:
            dmg = round(self.gladiator1.attack()) - self.gladiator2.toughness
            print(self.gladiator1.name + " attacked and did " + str(dmg) + " damage.")
            self.gladiator2.health -= dmg

        else:
            dmg = round(self.gladiator2.attack()) - self.gladiator1.toughness
            print(self.gladiator2.name + " attacked and did " + str(dmg) + " damage.")
            self.gladiator1.health -= dmg

        if self.gladiator1.health <= 0:
            print(
                self.gladiator2.name + " from " + self.team2.name + " killed " + self.gladiator1.name + " from " + self.team1.name)

        elif self.gladiator2.health <= 0:
            print(
                self.gladiator1.name + " from " + self.team1.name + " killed " + self.gladiator2.name + " from " + self.team2.name)

        else:
            print("Remaining health:\n\t" + self.gladiator1.name + ": " + str(self.gladiator1.health))
            print("Remaining health:\n\t" + self.gladiator2.name + ": " + str(self.gladiator2.health))
            print("No one died")
            print("\n\t\t******")

    def count_round(self):
        print("\n\n\t ROUND " + str(self.round_num) + "\n")
        self.round_num += 1

    def start_fight(self, t1: Team, t2: Team):
        if len(t1.gladiators) > 0 and len(t2.gladiators) > 0:
            gladiator1index = random.randint(0, len(t1.gladiators) - 1)
            gladiator2index = random.randint(0, len(t2.gladiators) - 1)
            self.gladiator1 = t1.gladiators[gladiator1index]
            self.gladiator2 = t2.gladiators[gladiator2index]
            self.team1 = t1
            self.team2 = t2

            print(
                self.gladiator1.name + " from " + t1.name + " is fighting " + self.gladiator2.name + " from " + t2.name)

            while len(t1.gladiators) > 0 and len(t2.gladiators) > 0:

                print("\n\t--- Press ENTER to fight! ---")
                next_fight = input()
                next_fight
                self.count_round()

                self.do_fight()
                if self.gladiator1.health <= 0:
                    del t1.gladiators[gladiator1index]
                    print(len(t1.gladiators), " & ", len(t2.gladiators))
                    self.start_fight(t1, t2)
                if self.gladiator2.health <= 0:
                    del t2.gladiators[gladiator2index]
                    print(len(t1.gladiators), " & ", len(t2.gladiators))
                    self.start_fight(t1, t2)

        if len(t1.gladiators) > 0:
            print("t1 winner")
        else:
            print("t2 winner")
