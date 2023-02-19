from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize webdriver
driver = webdriver.Chrome()

# Navigate to URL
driver.get("http://127.0.0.1:5500/textPropR1.html")

# Find the element containing the text
element = driver.find_element(By.CSS_SELECTOR, ".container")

# Get the text decoration style of the element
text_decoration = element.value_of_css_property("text-decoration")

# Check if the text is underlined
if "underline" in text_decoration:
    print("Text is underlined.")
else:
    print("Text is not underlined.")

# Close the webdriver
driver.quit()
