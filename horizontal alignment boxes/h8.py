from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# initialize the browser
driver = webdriver.Chrome()

# navigate to the page
driver.get("http://127.0.0.1:5500/indexR1.html") #css chapter 4
time.sleep(5)
# find the two elements you want to check for alignment
box1 = driver.find_element(By.XPATH, "//*[@id='box1']")
box2 = driver.find_element(By.XPATH, "//*[@id='box2']")

# get the left property of each element

left1 = box1.value_of_css_property("left")
left2 = box2.value_of_css_property("left")

width1 = box1.value_of_css_property("width")
width2 = box2.value_of_css_property("width")

if left1 == left2 :#and width1 == width2:
    print("Boxes are horizontally aligned and have the same width")
else:
    print("Boxes are not horizontally aligned or have different widths")


# close the browser
driver.quit()
