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

# get the location and size of each element
box1_location = box1.location
box1_size = box1.size

box2_location = box2.location
box2_size = box2.size

# check if the y-coordinate is the same for both elements
if box1_location['y'] == box2_location['y']:
    print("The boxes are horizontally aligned.")
else:
    print("The boxes are not horizontally aligned.")
    
# check if the size of the boxes are equal
if box1_size == box2_size:
    print("The boxes have the same size.")
else:
    print("The boxes have different size.")

# close the browser
driver.quit()
