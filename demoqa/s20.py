from selenium import webdriver
from selenium.webdriver.common.by import By
from decimal import Decimal

# Set up the Selenium driver (assuming you have already installed the driver)
driver = webdriver.Chrome()

# Load the HTML file with the example code
driver.get("http://127.0.0.1:5500/unitsMyR1.html")

# Find the <p> element with the "text" class
text_element = driver.find_element(By.CLASS_NAME, "text")

# Get the font size of the <p> element
font_size = text_element.value_of_css_property("font-size")

# Get the viewport width using JavaScript
viewport_width = driver.execute_script("return window.innerWidth")

print(viewport_width)
# Calculate the expected font size based on the viewport width
# expected_font_size = "{:.3f}px".format(int(viewport_width) * 0.05)

# Calculate the expected font size based on the viewport width, rounded to 3 decimal places
expected_font_size = round(float(viewport_width) * 0.1, 3)
expected_font_size = f"{expected_font_size}px"

# Print the actual and expected font sizes
print("Actual font size:", font_size)
print("Expected font size:", expected_font_size)

# Verify that the actual font size matches the expected value
assert font_size == expected_font_size, "Font size does not match expected value"

# Close the Selenium driver
driver.quit()
