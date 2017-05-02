from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By


class LoadOdds():
    DRIVER = webdriver.Firefox()
    BASE_URL = "https://www.bet365.com"
    WAIT_TIMER = 15

    def __init__(self):

        self.DRIVER.get(self.BASE_URL + "/en/?&cb=1032556542#/IP/")

    # first page will be a welcome page, need to click through some elements

    # --------------------- LOCATE ELEMENT SECTION ---------------------
    def locateElementByTextAndClick(self, element):
        try:
            WebDriverWait(self.DRIVER, self.WAIT_TIMER).until(EC.presence_of_element_located((By.LINK_TEXT, element)))
            self.DRIVER.find_element_by_link_text(element).click()

        except TimeoutException:
            # error handling
            print("Loading took too much time!-locateElementByTextAndClick")

    def locateElementByCssAndClick(self, element):
        try:
            WebDriverWait(self.DRIVER, self.WAIT_TIMER).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, element)))
            self.DRIVER.find_element_by_css_selector(element).click()

        except TimeoutException:
            # error handling
            print("Loading took too much time!-locateElementByCssAndClick")

    # --------------------- LOCATE ELEMENTS CLASS, CSS ---------------------

    def locateElementByCssAndLoad(self, element):
        try:
            WebDriverWait(self.DRIVER, self.WAIT_TIMER).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
            myElements = self.loadElementsByCssOnPage(element)
        except TimeoutException:
            # error handling
            print("Css element could not be found.")

            myElements = []

        return myElements

    def locateElementByClassAndLoad(self, element):
        try:
            WebDriverWait(self.DRIVER, self.WAIT_TIMER).until(EC.presence_of_element_located((By.CLASS_NAME, element)))
            myElements = self.loadElementsByClassOnPage(element)
        except TimeoutException:
            # error handling
            print("Class element could not be found.")
            myElements = []

        return myElements

    # --------------------- LOAD ELEMENTS INTO LIST CLASS, CSS ---------------------

    def loadElementsByClassOnPage(self, element):
        try:

            myOddList = self.DRIVER.find_elements_by_class_name(element)

        except WebDriverException as e:

            print(e)
            myOddList = []

        return myOddList

    def loadElementsByCssOnPage(self, element):
        try:

            myOddList = self.DRIVER.find_elements_by_css_selector(element)

        except WebDriverException as e:

            print(e)
            myOddList = []

        return myOddList
