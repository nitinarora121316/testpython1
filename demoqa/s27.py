from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Create an instance of the webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Navigate to a web page
driver.get("http://127.0.0.1:5500/demoqa/templates/dropdown.html")

# Wait for the dropdown element to be visible
dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "my-select"))
)

# Create a Select object for the dropdown
select = Select(dropdown)

# Generate random wait time between selections
wait_time = random.randint(1, 5)

# Set countdown timer to 30 seconds
countdown = 30

# Select all options one by one, with random wait time and countdown timer
for index in range(len(select.options)):
    select.select_by_index(index)
    print(f"Option {index+1} selected!")
    time.sleep(wait_time)
    countdown -= wait_time
    print(f"{countdown} seconds left!")
    if countdown <= 0:
        print("Time's up! Better luck next time.")
        driver.quit()
        break

# Congratulate the user on completing the challenge
if countdown > 0:
    print("Congratulations, you completed the dropdown selection challenge!")
    driver.quit()
