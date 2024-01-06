from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the web page that contains the list
driver.get("http://127.0.0.1:5500/practiceMyR1.html")

time.sleep(2)

# Find the list items using the By class
lis = driver.find_elements(By.TAG_NAME, "li")

# Get the value of the "list-style" property of the first list item
list_style = lis[0].value_of_css_property("list-style")

print(list_style)

# Verify that the list style is "circle"
# assert list_style == "circle"
assert "circle" in list_style.split()


# Close the browser
driver.quit()
