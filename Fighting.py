import Team
import random

class Fighting:

    gladiator1 = "Gladiator_1"
    gladiator2 = "Gladiator_2"

    gladiator1_toughness = 100
    gladiator2_toughness = 100

    def print_result_text(self):
        print("The fight ended with \n\n" + self.gladiator1 + " - " + self.gladiator2
              + " " + str(self.gladiator1_toughness) + " : " + str(self.gladiator2_toughness))


    def start_fight(self, t1: Team, t2: Team):
        self.gladiator1 = t1.gladiators[random.randint(0, 3)].name
        self.gladiator2 = t2.gladiators[random.randint(0, 3)].name
        self.gladiator1_toughness = t1.gladiator1.toughness
        self.gladiator2_toughness = t2.gladiator2.toughness
