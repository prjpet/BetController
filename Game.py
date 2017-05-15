#inherit ALL properties

class Game(object):

    firstTeam = "unkown"
    secondTeam = "unkown"
    time = "unknown"
    bet = False

    listOfPossibleBets = []

    def __init__(self, team1, team2):
        self.setFirstTeam(team1)
        self.setSecondTeam(team2)

    def appendBet(self, bet):
        self.listOfPossibleBets.append(bet)

    def setFirstTeam(self, teamName):

        self.firstTeam = teamName

    def setSecondTeam(self, teamName):

        self.secondTeam = teamName


    def setTime(self, currentTime):
        self.time = currentTime

    def getFirstTeam(self):
        return self.firstTeam

    def getSecondTeam(self):
        return self.secondTeam

    def getTime(self):
        return self.time

    def getPossibleBets(self, bet):
        return self.listOfPossibleBets


    def toString(self):

        print("First Team: ", self.getFirstTeam(), "Second Team: ", self.getSecondTeam(), "Time: ", self.getTime())
