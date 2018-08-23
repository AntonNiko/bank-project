from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exception import NoSuchElementException

import sys
sys.path.insert(0, "../")
import manage

CHROME_DRIVER_PATH = "chromedriver.exe"
FIREFOX_DRIVER_PATH = "geckodriver.exe"

LOGIN_TESTS_FILE = "login_tests.txt"

class Driver():
    """
    Class which runs the automated web testing software and evaluates the success of these tests
    """

    def __init__(self, driver_exe_path):
        self.driver = webdriver.Chrome()
        self.loadLoginFile(LOGIN_TESTS_FILE)
        self.driver.get("http://127.0.0.1:8080/publicbanking/")

        self.enterLoginInformation("aa","bb")
        self.submitLoginInformation()

    def enterLoginInformation(self, card, password):
        """
        Function which finds the card and password fields of the login page, and enters the arguments provided
        in the elements

        Args:
            card (str): Card Number for login purposes
            password (str): Password for account
        Returns:
            result (bool): Indicates if the information was entered successfully
            
        """
        try:
            cardField = self.driver.find_element_by_id("card_number")
            passwordField = self.driver.find_element_by_id("card_password")
            cardField.send_keys(card)
            passwordField.send_keys(password)
            result = True
        except NoSuchElementException:
            result = False

        return result

    def submitLoginInformation(self):
        submitButton = self.driver.find_element_by_id("login_submit")
        submitButton.click()

    def loadLoginFile(self, filename):
        self.loginInfo = []
        with open(filename, "r") as f:
            for line in f:
                self.loginInfo.append(line.split(","))
        
        
if __name__ == "__main__":
    test_driver = Driver(CHROME_DRIVER_PATH)
