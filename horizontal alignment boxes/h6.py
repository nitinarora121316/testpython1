from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# initialize the browser
driver = webdriver.Chrome()

# navigate to the page
driver.get("http://127.0.0.1:5500/indexR1.html")

time.sleep(3)

# find the two elements you want to check for alignment
box1 = driver.find_element(By.XPATH, "//*[@id='box1']")
box2 = driver.find_element(By.XPATH, "//*[@id='box2']")

# get the location of each element
box1_location = box1.location
box2_location = box2.location

# check if the y-coordinate is the same for both elements
if box1_location['y'] == box2_location['y']:
    print("The boxes are horizontally aligned.")
else:
    print("The boxes are not horizontally aligned.")

# close the browser
driver.quit()
