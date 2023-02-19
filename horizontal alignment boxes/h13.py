import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Load the Excel workbook and access the worksheet with the locators
# workbook = openpyxl.load_workbook("C:\\Users\\asus\\Desktop\\locators.xlsx")
workbook = openpyxl.load_workbook("locators.xlsx")
worksheet = workbook["Sheet2"]

# Get the locators from the worksheet
toggle_button_locator = worksheet["B2"].value
text_locator = worksheet["B3"].value

print(toggle_button_locator)
print(text_locator)

# Initialize a new browser instance
driver = webdriver.Chrome()

# Navigate to the website
driver.get("http://127.0.0.1:5500/indexR1_2.html")
time.sleep(2)

# Find the toggle button by its locator and click on it
toggle_button = driver.find_element(By.ID, toggle_button_locator)
toggle_button.click()
time.sleep(2)

# Verify that the text is now hidden
text = driver.find_element(By.ID, text_locator)
assert text.get_attribute("class") == ""

# Close the browser
driver.quit()
