from selenium import webdriver
from selenium.webdriver.common.by import By


# Set up the Selenium driver (assuming you have already installed the driver)
driver = webdriver.Chrome()

# Load the HTML file with the example code
driver.get("http://127.0.0.1:5500/1.html")

# Get the <p> element with the "em-example" class
em_p = driver.find_element(By.CLASS_NAME,"em-example")

# Get the font size of the <p> element in pixels
font_size = em_p.value_of_css_property("font-size")

# Check that the font size is 24 pixels
assert font_size == "24px", f"Unexpected font size: {font_size}"


# Print a message if the assertion passes
print("Font size is 24px as expected.")

# Close the Selenium driver
driver.quit()
