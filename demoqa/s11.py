from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create an instance of Chrome WebDriver
# driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)


# Navigate to the webpage
driver.get("http://127.0.0.1:5500/chapter4PsR1.html#")
time.sleep(2)

# Find the header tag using By.TAG_NAME and check that its text is aligned to the left
header = driver.find_element(By.TAG_NAME, "header")
assert header.value_of_css_property("text-align") == "left"

# Find all the links in the header and check that they are left-aligned
links = header.find_elements(By.TAG_NAME, "a")
for link in links:
    assert link.value_of_css_property("text-align") == "left"

# Close the browser window
driver.quit()
