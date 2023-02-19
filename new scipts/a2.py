from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

driver = webdriver.Firefox()
driver.get("https://www.google.com")

print("Guess the number between 1 and 100:")
target_num = random.randint(1, 100)

while True:
    user_input = driver.find_element(By.NAME, "q")
    user_input.send_keys(input("Enter your guess: "))
    user_input.send_keys(Keys.RETURN)
    driver.implicitly_wait(1)

    if int(user_input.get_attribute("value")) == target_num:
        print("You've guessed it right!")
        break
    elif int(user_input.get_attribute("value")) < target_num:
        print("The target number is greater than your guess.")
    else:
        print("The target number is smaller than your guess.")

driver.quit()
