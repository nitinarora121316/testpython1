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

# Get all the options from the dropdown
options = select.options

# Loop through each option and print its text while selecting it
for option in options:
    option_text = option.text
    print(f"Selecting option: {option_text}")
    select.select_by_visible_text(option_text)
    time.sleep(2)
