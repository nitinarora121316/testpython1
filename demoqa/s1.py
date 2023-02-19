from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Class1:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class PersonPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_field = (By.XPATH, '//input[@id="firstName"]')
        self.last_name_field = (By.XPATH, '//input[@id="lastName"]')

    def fill_person_details(self, person):
        self.driver.find_element(*self.first_name_field).send_keys(person.first_name)
        self.driver.find_element(*self.last_name_field).send_keys(person.last_name)

def main():
    driver = webdriver.Chrome()
    person_page = PersonPage(driver)
    person = Class1("John", "Doe")

    driver.get("https://demoqa.com/automation-practice-form")
    person_page.fill_person_details(person)

    print("Person details filled successfully!")
    time.sleep(2)
    driver.quit()

if __name__ == "__main__":
    main()
