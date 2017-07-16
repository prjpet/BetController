class WebsiteNavigator:

    def __init__(self, LoadBrowser):

        self.LoadBrowser = LoadBrowser


    def navigateToGames(self):
        # 1. PREPARE WEBSITE:
        # - Click through the correct links until on the correct page (Overview - Soccer)
        # missing: delay between interaction
        self.LoadBrowser.locateElementByTextAndClick("English")

        self.LoadBrowser.locateElementByTextAndClick("In-Play")
        self.LoadBrowser.DRIVER.find_elements_by_class_name("hm-DropDownSelections_Highlight ")[1].click()
        self.LoadBrowser.locateElementByTextAndClick("Decimal")

        # 3. CLICK "Event View"
        self.LoadBrowser.locateElementByXpathAndClick("//span/div[2]")

    def login(self):
        print("login function called")
        # 2. LOGIN

        # LoadOdds.locateUsernameAndPassword("input.hm-Login_InputField", "username","password")
        # LoadOdds.locateElementByCssAndClick("button.hm-Login_LoginBtn")