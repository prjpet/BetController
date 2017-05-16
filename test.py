from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class LogIn(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.bet365.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_log_in(self):
        driver = self.driver
        driver.get(self.base_url + "/#/IP/")
        driver.find_element_by_link_text("English").click()
        driver.find_element_by_link_text("In-Play").click()

        driver.find_element_by_css_selector("input.hm-Login_InputField.").clear()
        driver.find_element_by_css_selector("input.hm-Login_InputField.").send_keys("alexandra1188")

        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("indietro11")

        driver.find_element_by_css_selector("button.hm-Login_LoginBtn.hm-Login_LoginBtnFocused").click()

        flag = 1

        while (flag): print
        'Given flag is really true!'

        print
        "Good bye!"

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

        flag = 1

        while (flag): print
        'Given flag is really true!'

        print
        "Good bye!"


if __name__ == "__main__":
    unittest.main()