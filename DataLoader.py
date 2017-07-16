import datetime, time


class DataLoader:

    #INTERNAL VARIABLES
    Odd05_first_half = None
    Odd05_second_half = None
    OverGoals = None
    Winner = None
    Bet_ON = None
    Bet_ON_List = None
    Item_Found = None
    Half = None

    #STRATEGIC VARIABLES
    # First HALF XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXx
    StartTime1 = 5  # First minute that is permited to bet on FIRST half
    EndTime1 = 45  # Last minute that is permiteted to bet on FIRST half
    MinValOdd1 = "1.2"  # Minimum value for the odd that is permited to bet on FIRST half

    # Second HALF XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXx
    StartTime2 = 48  # First minute that is permited to bet on SECOND half
    EndTime2 = 85  # Last minute that is permiteted to bet on SECOND half
    MinValOdd2 = "1.2"  # Minimum value for the odd that is permited to bet on SECOND half

    def __init__(self, LoadBrowser, StartTime1, EndTime1, MinValOdd1,  StartTime2, EndTime2, MinValOdd2):

        self.LoadBrowser = LoadBrowser

        self.StartTime1 = StartTime1
        self.EndTime1 = EndTime1
        self.MinValOdd1 = MinValOdd1

        self.StartTime2 = StartTime2
        self.EndTime2 = EndTime2
        self.MinValOdd2 = MinValOdd2

    def printToList(self, file, whatToPrint, winOrLose):
        """

        :param file: string of characters that gives the beginning of the file name
        :param whatToPrint:
        :param max_i:
        """

        File1 = file + '_' + str(datetime.datetime.now().strftime("%d_%m_%Y")) + '.txt'
        with open(File1, 'a') as file:
            file.write(str(whatToPrint))
            file.write(str(winOrLose))
            file.write('\n')
            file.close()

    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


    def gatherOddData(self, item1, current_i, max_i, startProgramTime):
        """

        :param item1:
        :param current_i:
        :param max_i:
        """

        splitText = item1.text.split("\n")

        if len(splitText) >= 4:

            Team1 = splitText[0]
            Team2 = splitText[1]
            Score = splitText[2]
            GameTime = splitText[3]
        else:

            Team1 = "NONE"
            Team2 = "NONE"
            Score = "NONE"
            GameTime = "NONE"

        # LOOK FOR FIRST HALF GOALS
        SEARCH_STRING1 = "First Half Goals"
        SEARCH_STRING2 = "Over"
        SEARCH_STRING3 = "Match Goals"

        # MARKET_GROUP is the full list of odds
        ListOfOdds = self.LoadBrowser.locateElementsByClassAndLoad("gl-MarketGroup")

        try:
            # Search for First Half Odds
            if 0 < int(GameTime[:2]) and Score == "0-0":
                for i, item in enumerate(ListOfOdds):


                    if ListOfOdds == self.LoadBrowser.locateElementsByClassAndLoad("gl-MarketGroup") and (
                        item.text.find(SEARCH_STRING1) != -1):
                        FHG_list = item.text.split("\n")

                        # check if Over value is a float value- error in case that odds are blocked/modified
                        if FHG_list[FHG_list.index(SEARCH_STRING2) + 1] != "Under":

                            self.Odd05_first_half = FHG_list[FHG_list.index(SEARCH_STRING2) + 1]
                            self.OverGoals = (FHG_list[1])
                            break

                            # Search for Second Half Odds
            if 45 < int(GameTime[:2]) and Score == "0-0":
                for i, item in enumerate(ListOfOdds):


                    if ListOfOdds == self.LoadBrowser.locateElementsByClassAndLoad("gl-MarketGroup") and (
                        item.text.find(SEARCH_STRING3) != -1):
                        FHG_list = item.text.split("\n")

                        # check if Over value is a float value- error in case that odds are blocked/modified
                        if FHG_list[FHG_list.index(SEARCH_STRING2) + 1] != "Under":

                            self.Odd05_second_half = FHG_list[FHG_list.index(SEARCH_STRING2) + 1]
                            self.OverGoals = (FHG_list[1])
                            break

        except Exception as e:
            print("Exception occured with ", e)

        # Validate for bet_on for FIRST HALF
        if Score == "0-0" and 0 < int(GameTime[:2]) < 45:
            self.Half = "First"
        # Validate for bet_on for SECOND HALF
        if Score == "0-0" and 45 < int(GameTime[:2]):
            self.Half = "Second"

        if self.Odd05_second_half == "NONE":
            self.Odd05 = self.Odd05_first_half
        else:
            self.Odd05 = self.Odd05_second_half

        BotTime = ((time.time() - startProgramTime) / 60)

        # element_list with: CURRENT TIME.....RUN TIME.....TEAM 1.....TEAM 2.....SCORE.....TIME OF THE GAME.....OVER GOALS....ODD OVER.....BET ON.....Which half


        element_list = [datetime.datetime.now(), "%.2f" % BotTime, current_i, "out of", max_i, Team1, Team2, Score,
                        GameTime, self.OverGoals, self.Odd05, self.Bet_ON, self.Half]

        if element_list[7] == "0-0" and element_list[10] != "NONE":
            self.printToList('GATHER_ON_LIST', element_list, "")
            print(element_list[1:])

            # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

