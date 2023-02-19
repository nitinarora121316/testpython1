from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/indexR1_2.html")  #css script chapter 4 

element = driver.find_element(By.ID, "myId")
class_name = element.get_attribute("class")
if "hide-me" in class_name:
    print("Element is not visible")
else:
    print("Element is visible")

driver.quit()
