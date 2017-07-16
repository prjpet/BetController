from DataLoader import DataLoader
import pyautogui, gc

from DataLoader import DataLoader


class GameListNavigator:


    def __init__(self, LoadBrowser, simulation, StartTime1, EndTime1, MinValOdd1,  StartTime2, EndTime2, MinValOdd2, startProgramTime):
        self.simulation = simulation
        self.LoadBrowser = LoadBrowser
        pyautogui.hotkey('win', 'right')
        self.startProgramTime = startProgramTime
        self.DataLoader = DataLoader(LoadBrowser, StartTime1, EndTime1, MinValOdd1,  StartTime2, EndTime2, MinValOdd2)




    def getNextGameData(self):
        originalGames = self.LoadBrowser.locateElementsByClassAndLoad("ipn-FixtureButton ")

        if originalGames != "":
            print("While loop restarted----------------Reason: Beginning of list reached ")
            itemCounter = 0
            gc.collect() # garbage collect- clear memory

            #METHOD:
            #    - the game list is containing all games not just football so need to filter: score length, time length and something else...
            try:
                # ASSUMPTION: LIST IS VALID Counter is not exceed and Sore lenght is 3 (as a normal football game) and lists haven't changed
                while len(originalGames[itemCounter].text.split("\n")) >= 3 and \
                      len(originalGames) > itemCounter + 1 and len(originalGames[itemCounter].text.split("\n")[2]) == 3 and \
                      len(originalGames[itemCounter].text.split("\n")[3]) == 5:

                    # MOVE TO CORRECT POSITION:
                    moveToX = originalGames[itemCounter].location_once_scrolled_into_view['x'] + pyautogui.size()[0] / 2 + 100
                    moveToY = originalGames[itemCounter].location_once_scrolled_into_view['y'] + 120

                    # move cursor to begining of the list
                    if itemCounter == 0: pyautogui.moveTo(moveToX, moveToY, duration=0.5)

                    # CLICK:
                    pyautogui.click(button='left')

                    # LOAD DATA Option BET_ON
                    if self.simulation: self.DataLoader.gatherOddData(originalGames[itemCounter], itemCounter, len(originalGames), self.startProgramTime)
                    # LOAD DATA Option Gather_Data
                    #else:  DataLoader.loadOddData(self.originalGames[itemCounter], itemCounter, len(self.originalGames, self.startProgramTime))

                    itemCounter += 1

            except Exception as e:
                print("While loop encounted some error, loop restarted", e)
                pass

        #corrected indentation here - PP 15/07/2017
        else:
            print("GameList is null")
