from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

# Open the web page
driver.get("http://127.0.0.1:5500/other%20scripts%202/3.html")

# Locate the elements using By class
field1_element = driver.find_element(By.ID, "field1")
field2_element = driver.find_element(By.ID, "field2")

# Verify that "Hello World" is present in Field 1
assert field1_element.get_attribute("value") == "Hello World"

# Double click on Field 2
actions = ActionChains(driver)
actions.double_click(field2_element).perform()
time.sleep(2)

# Verify that the text from Field 1 is copied to Field 2
assert field2_element.get_attribute("value") == "Hello World"

# Close the browser
driver.quit()
