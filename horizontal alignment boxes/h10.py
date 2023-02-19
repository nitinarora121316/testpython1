from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# initialize the browser
driver = webdriver.Chrome()

# navigate to the page
driver.get("http://127.0.0.1:5500/indexR1.html") #css chapter 4

time.sleep(3)

# find the two elements you want to check for alignment
box1 = driver.find_element(By.XPATH, "//*[@id='box1']")
box2 = driver.find_element(By.XPATH, "//*[@id='box2']")
container = driver.find_element(By.CLASS_NAME, "container")

display1 = box1.value_of_css_property("display")
display2 = box2.value_of_css_property("display")
display3 = container.value_of_css_property("display")

if (display1 == "inline" or display1 == "inline-block"  or display3=="flex") and (display2 == "inline" or display2 == "inline-block"  or display3=="flex"):
    print("Boxes are horizontally aligned")
else:
    print("Boxes are not horizontally aligned")


# close the browser
driver.quit()
