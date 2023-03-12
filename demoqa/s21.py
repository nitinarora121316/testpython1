from selenium import webdriver
from selenium.webdriver.common.by import By
from decimal import Decimal
import random

# Set up the Selenium driver (assuming you have already installed the driver)
# driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Prompt the user to input the URL
url = input("Enter the URL of the HTML file: ")
driver.get(url)

# Find the <p> element with the "text" class
text_element = driver.find_element(By.CLASS_NAME, "text")

# Get the font size of the <p> element
font_size = text_element.value_of_css_property("font-size")

# Get the viewport width using JavaScript
viewport_width = driver.execute_script("return window.innerWidth")

# Randomize the expected font size as a percentage of the viewport width
expected_percentage = random.uniform(5, 11)
expected_font_size = round(float(viewport_width) * expected_percentage / 100, 3)
expected_font_size = f"{expected_font_size}px"

# Print the actual and expected font sizes
print("Actual font size:", font_size)
print("Expected font size:", expected_font_size)

# Define an acceptable range as +/- 2px
acceptable_range = 2

# Convert the font sizes to decimal numbers for comparison
font_size_decimal = Decimal(font_size[:-2])
expected_font_size_decimal = Decimal(expected_font_size[:-2])

# Determine whether the actual font size is within the acceptable range of the expected value
if abs(font_size_decimal - expected_font_size_decimal) <= acceptable_range:
    print("Font size is within acceptable range.")
else:
    print("Font size is not within acceptable range.")

# Close the Selenium driver
driver.quit()
