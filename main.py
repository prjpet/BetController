# USER VARIABLES

# First HALF XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXx
StartTime1 = 5 # First minute that is permited to bet on FIRST half
EndTime1 = 45  # Last minute that is permiteted to bet on FIRST half
MinValOdd1 = "1.2"  # Minimum value for the odd that is permited to bet on FIRST half

# Second HALF XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXx
StartTime2 = 48  # First minute that is permited to bet on SECOND half
EndTime2 = 85  # Last minute that is permiteted to bet on SECOND half
MinValOdd2 = "1.2"  # Minimum value for the odd that is permited to bet on SECOND half

minDelay = 4  # Minumum time delay in seconds
MaxDelay = 10  # Maximum time delay in seconds
START_OFFSET = 225

global Debug, Debug2, Bet_Option
Debug=False
Debug2=True
Bet_Option=2    # 1- Bet option as BET_ON,  2-Gather  data,


from BrowserLoader import BrowserLoader
from WebsiteNavigator import WebsiteNavigator
from GameListNavigator import GameListNavigator
import random, time, pyautogui, gc, datetime


# When fail-safe mode is True, moving the mouse to the upper-left will raise a pyautogui.FailSafeException that can abort your program:
pyautogui.FAILSAFE = True
a = random.uniform(minDelay, MaxDelay)  # example of Random time delay

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX





if __name__ == "__main__":

    LoadBrowser = BrowserLoader()

    WebsiteNavigator = WebsiteNavigator(LoadBrowser)

    WebsiteNavigator.navigateToGames()

    # used for debugging purpose
    startProgramTime = time.time()

    GameListNavigator = GameListNavigator(LoadBrowser, True, StartTime1, EndTime1, MinValOdd1,  StartTime2, EndTime2, \
                                          MinValOdd2, startProgramTime)

    while True: 
        try:
            GameListNavigator.getNextGameData()
        except Exception as e:
            print("The program now exits. ", e)
            break

























        # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
