import Fighting
import Team
import Lanista


Team1 = Team.Team("The House of Horror")
Team2 = Team.Team("The Brotherhood")


Team1.printteam()
Team2.printteam()

fight = Fighting.Fighting()
fight.start_fight(Team1, Team2)
#if len(Team1.gladiators) > 0:
  #  print("\n" + Team1.name + " HAVE WON THE FIGHT")
#else:
    #print("\n" + Team2.name + " HAVE WON THE FIGHT")