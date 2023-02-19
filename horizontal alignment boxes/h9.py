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

# get the margin-left property of each element
box1_margin_left = box1.get_attribute('style').split(';')[0].split(':')[1]
box2_margin_left = box2.get_attribute('style').split(';')[0].split(':')[1]

# check if the margin-left property is the same for both elements
if box1_margin_left == box2_margin_left:
    print("The boxes are horizontally aligned.")
else:
    print("The boxes are not horizontally aligned.")

# close the browser
driver.quit()
