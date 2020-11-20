from Lanista import *
import SwordMan
import SpearMan


class Team:
    names = ["Atticus", "Augustus", "Aurelius", "Claudius", "Julius", "Hadrian", "Magnus", "Marcellus",
             "Maximus", "Octavius", "Judas", "Jesus", "Romanus", "Pseudolus", "Alexandru", "Auxilium", "Augustinus",
             "Felicius"]

    titles = ["the Crooked", "the Bonemachine", "the Vicious", "Iron Grip", "Tough Stuff", "the Impure", "the Screamer",
              "the Diseased", "the Deceased", "Skullmantle", "Ragestare", "Bonecrusher", "Ironbrow", "the Agonizer",
              "the Chosen", "Potter", "Death Mane", "the Feral", "the Drake", "Dragonborn", "Ironfist", "the Betrayer",
              "the Glutenous"]

    lan_names = [""]

    def __init__(self, name: str):
        self.name = name
        self.lan_names = "Bob"
        # Lanista.Lanista([random.randint(0, len(self.names)-1)])
        self.gladiators = []

        for i in range(3):
            randomName = random.randint(0, len(self.names) - 1)
            randomTitle = random.randint(0, len(self.titles) - 1)
            self.gladiators.append(SwordMan.SwordMan(self.names[randomName],
                                                     (self.titles[randomTitle])))

        for i in range(3):
            randomName = random.randint(0, len(self.names) - 1)
            randomTitle = random.randint(0, len(self.titles) - 1)
            self.gladiators.append(SpearMan.SpearMan(self.names[randomName],
                                                     (self.titles[randomTitle])))

    def printteam(self):
        print("\nINFO ABOUT: " + str(self.name))
        print("NUMBER OF GLADIATORS " + str(len(self.gladiators)))
        self.gladiators.sort(key=lambda x: x.name)
        for gladiators in self.gladiators:
            gladiators.printinfo()
        print("\n------------------------------------------------")

    def print_fighter(self, num: int):
        self.gladiators[num].printinfo()
