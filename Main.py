import Fighting
import Team as Team
import Lanista

TeamDuckster = Team.Team("Duckster", Lanista.Lanista("Johannes"))
TeamKitsy = Team.Team("Kitsy", Lanista.Lanista("Christian"))

TeamDuckster.print_team()
TeamKitsy.print_team()

fight = Fighting.Fighting()
fight.start_fight(TeamDuckster, TeamKitsy)

