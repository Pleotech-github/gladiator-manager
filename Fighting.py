import Team
import random


class Fighting:
    team1 = ""
    team2 = ""
    turn = 0
    gladiator1 = "Gladiator_1"
    gladiator2 = "Gladiator_2"

    round_num = 1

    def do_fight(self):

        if random.randint(0, 1) == 1:
            dmg = round(self.gladiator1.attack()) - self.gladiator2.toughness
            print(self.gladiator1.name + " attacked and did " + str(dmg) + " damage.\n")
            self.gladiator2.health -= dmg

        else:
            dmg = round(self.gladiator2.attack()) - self.gladiator1.toughness
            print(self.gladiator2.name + " attacked and did " + str(dmg) + " damage.\n")
            self.gladiator1.health -= dmg

        if self.gladiator1.health <= 0:
            print("REMAINING HEALTH:\n\t" + self.gladiator1.name + ": " + str(self.gladiator1.health))
            print("REMAINING HEALTH:\n\t" + self.gladiator2.name + ": " + str(self.gladiator2.health))
            print(
                "\n"+self.gladiator2.name + " " + self.gladiator2.title + " from " + self.team2.name +
                      "\nKILLED \n" + self.gladiator1.name + " " + self.gladiator1.title + " from " + self.team1.name)

        elif self.gladiator2.health <= 0:
            print("REMAINING HEALTH:\n\t" + self.gladiator1.name + ": " + str(self.gladiator1.health))
            print("REMAINING HEALTH:\n\t" + self.gladiator2.name + ": " + str(self.gladiator2.health))
            print(
                "\n"+self.gladiator1.name + " " + self.gladiator1.title + " from " + self.team1.name +
                      "\n\t\tHAVE KILLED \n" + self.gladiator2.name + " " + self.gladiator2.title + " from" + self.team2.name)

        else:
            print("REMAINING HEALTH:\n\t" + self.gladiator1.name + ": " + str(self.gladiator1.health))
            print("REMAINING HEALTH:\n\t" + self.gladiator2.name + ": " + str(self.gladiator2.health))
            print("\nNO ONE DIED!")
            # print("\n\t\t******")

    def count_round(self):
        print("\t\t ROUND " + str(self.round_num) + "\n")
        self.round_num += 1

    def set_fighters(self, t1: Team, t2: Team):
        if len(t1.gladiators) > 0 and len(t2.gladiators) > 0:
            gladiator1index = random.randint(0, len(t1.gladiators) - 1)
            gladiator2index = random.randint(0, len(t2.gladiators) - 1)
            self.gladiator1 = t1.gladiators[gladiator1index]
            self.gladiator2 = t2.gladiators[gladiator2index]
            self.team1 = t1
            self.team2 = t2

            print("\n" +
                self.gladiator1.name + " " + self.gladiator1.title + " from " + t1.name + "\n\t\tVS \n" +
                self.gladiator2.name + " " + self.gladiator2.title + " from " + t2.name)
            return gladiator1index, gladiator2index
        else:
            if len(t1.gladiators) > 0:
                print("\n" + t1.name + " HAVE WON THE FIGHT")
            else:
                print("\n" + t2.name + " HAVE WON THE FIGHT")
            return -1, -1

    def turns(self,action):
        if action:
            if self.turn == 1:
                self.turn = 0
            else:
                self.turn = 1
        return self.turn

    def start_fight(self, t1: Team, t2: Team):
            index1, index2 = self.set_fighters(t1, t2)
            if len(t1.gladiators) > 0 and len(t2.gladiators) > 0:
                print("\n\t--- Press ENTER to fight! ---")
                self.turns(True)
                self.count_round()
                self.do_fight()
                if self.gladiator1.health <= 0:
                    del t1.gladiators[index1]
                    print("\n" + t1.name + " have " + str(len(t1.gladiators)) + " gladiators left.\n" + t2.name +
                          " have " + str(len(t2.gladiators)) + " gladiators left.")
                    print("\n\t\t******")
                    index1, index2 = self.set_fighters(t1, t2)
                if self.gladiator2.health <= 0:
                    del t2.gladiators[index2]
                    print("\n" + t1.name + " have " + str(len(t1.gladiators)) + " gladiators left.\n" + t2.name +
                          " have " + str(len(t2.gladiators)) + " gladiators left.")
                    print("\n\t\t******")
                    index1, index2 = self.set_fighters(t1, t2)
