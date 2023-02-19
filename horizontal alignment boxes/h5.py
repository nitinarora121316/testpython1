from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/indexR1_2.html") #css script chapter 4 
time.sleep(2)


# Find the toggle button by its ID and click on it
toggle_button = driver.find_element(By.ID,"toggle-button")
toggle_button.click()
time.sleep(2)

# Verify that the text is now hidden
text = driver.find_element(By.ID, "myId")
assert text.get_attribute("class") == "hide-me"
driver.quit()


# element = driver.find_element(By.ID, "myId")
# class_name = element.get_attribute("class")
# if "hide-me" in class_name:
#     print("Element is not visible")
# else:
#     print("Element is visible")

# driver.quit()
