import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By

# Load the Excel file and get the locator information
wb = openpyxl.load_workbook("locators.xlsx")
sheet = wb["Sheet3"]

locator_type = sheet["B2"].value
locator_value = sheet["B3"].value

# Initialize webdriver
driver = webdriver.Chrome()

# Navigate to URL
driver.get("http://127.0.0.1:5500/textPropR1.html")

# Get the By type based on the locator type from the Excel sheet
by_type = None
if locator_type == "css_selector":
    by_type = By.CSS_SELECTOR

# Find the element using the locator value and By type
element = driver.find_element(by_type, locator_value)
# element = driver.find_element(By.CSS_SELECTOR, locator_value)

# Get the text decoration style of the element
text_decoration = element.value_of_css_property("text-decoration")

# Check if the text is underlined
if "underline" in text_decoration:
    print("Text is underlined.")
else:
    print("Text is not underlined.")

# Close the webdriver
driver.quit()
