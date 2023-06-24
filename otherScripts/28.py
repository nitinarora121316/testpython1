from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

class SuiteTests:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service("path/to/chromedriver.exe"))
        
    def setup(self):
        self.driver.maximize_window()
        
    def teardown(self):
        self.driver.quit()
        
    def test_case1(self):
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.find_element(By.ID, "firstName").click()
        self.driver.find_element(By.ID, "firstName").send_keys("hello")
        time.sleep(5)
        self.driver.find_element(By.ID, "lastName").click()
        self.driver.find_element(By.ID, "lastName").send_keys("arora")
        # self.driver.find_element(By.CSS_SELECTOR, ".custom-radio:nth-child(1) > .custom-control-label").click()
        self.driver.find_element(By.ID, "userEmail").click()
        self.driver.find_element(By.ID, "userEmail").send_keys("abc@gmail.com")
        self.driver.find_element(By.ID, "userNumber").click()
        self.driver.find_element(By.ID, "userNumber").send_keys("12332323")
        # self.driver.find_element(By.CSS_SELECTOR, ".custom-checkbox:nth-child(1) > .custom-control-label").click()
        time.sleep(5)

# Create an instance of the test suite
suite = SuiteTests()

# Setup the driver and perform the test case
suite.setup()
suite.test_case1()

# Tear down the driver
suite.teardown()
