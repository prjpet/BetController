#inherit ALL properties

class Game(object):

    firstTeam = "unkown"
    secondTeam = "unkown"
    time = "unknown"
    score = "unknown"
    bet = False

    listOfPossibleBets = []

    def __init__(self, team1, team2, time="unknown", score="unknown"):
        self.setFirstTeam(team1)
        self.setSecondTeam(team2)
        self.setTime(time)
        self.setScore(score)

    def appendBet(self, bet):
        self.listOfPossibleBets.append(bet)

    def setFirstTeam(self, teamName):

        self.firstTeam = teamName

    def setSecondTeam(self, teamName):

        self.secondTeam = teamName


    def setTime(self, currentTime):
        self.time = currentTime

    def setScore(self, score):
        self.score = score

    def getFirstTeam(self):
        return self.firstTeam

    def getSecondTeam(self):
        return self.secondTeam

    def getTime(self):
        return self.time

    def getScore(self):
        return self.score

    def getPossibleBets(self, bet):
        return self.listOfPossibleBets


    def toString(self):

        print("First Team: ", self.getFirstTeam(), " - Second Team: ", self.getSecondTeam(), " - Time: ", self.getTime(), " - Score: ", self.getScore(), "\n")
