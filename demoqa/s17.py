from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Selenium driver (assuming you have already installed the driver)
driver = webdriver.Chrome()

# Load the HTML file with the example code
driver.get("http://127.0.0.1:5500/1.html")

# Get the <p> element with the "em-example" class
em_p = driver.find_element(By.CLASS_NAME, "em-example")

# Get the computed font size of the <p> element in pixels
parent_font_size = driver.execute_script("return window.getComputedStyle(arguments[0].parentNode).getPropertyValue('font-size');", em_p)
print(parent_font_size)
font_size = em_p.value_of_css_property("font-size")

# Calculate the expected font size in pixels    
expected_size = str(int(round(float(parent_font_size[:-2]) * 1.5))) + "px"
print(expected_size)

# Check that the font size is 1.5em of the parent font size
assert font_size == expected_size, f"Unexpected font size: {font_size}. Expected: {expected_size}"

# Print a message if the assertion passes
print("Font size is 1.5em of parent font size as expected.")

# Close the Selenium driver
driver.quit()
