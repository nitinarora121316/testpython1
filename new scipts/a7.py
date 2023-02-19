import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Load the Excel file and get the locator information
wb = openpyxl.load_workbook("locators.xlsx")
sheet = wb["Sheet3"]

locator_type = sheet["B2"].value
locator_value = sheet["B3"].value

# Initialize webdriver
driver = webdriver.Chrome()

# Navigate to URL
driver.get("http://127.0.0.1:5500/textPropR1.html")
time.sleep(1)

# Get the By type based on the locator type from the Excel sheet
by_type = None
if locator_type == "css_selector":
    by_type = By.CSS_SELECTOR

# Find the element using the locator value and By type
element = driver.find_element(by_type, locator_value)

# Get the font-family of the element
font_family = element.value_of_css_property("font-family")
print(font_family)

# Assert that the font family is one of the three font families
assert "Courier New" in font_family or "Courier" in font_family or "monospace" in font_family, f"Expected font family not found. Found: {font_family}"

# Close the webdriver
driver.quit()
