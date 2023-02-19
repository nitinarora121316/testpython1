from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize webdriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("http://127.0.0.1:5500/indexR1.html") #css chapter 4

time.sleep(3)
# find the two elements you want to check for alignment
box1 = driver.find_element(By.XPATH, "//*[@id='box1']")
box2 = driver.find_element(By.XPATH, "//*[@id='box2']")

# Get the display property of the container
container_display = driver.execute_script("return window.getComputedStyle(document.querySelector('.container'),null).getPropertyValue('display')")

# Get the justify-content property of the container if it is grid layout
justify_content = driver.execute_script("return window.getComputedStyle(document.querySelector('.container'),null).getPropertyValue('justify-content')")

# Get the align-items property of the container if it is flex layout
align_items = driver.execute_script("return window.getComputedStyle(document.querySelector('.container'),null).getPropertyValue('align-items')")

# Check if the boxes are horizontally aligned
if container_display == "grid" and justify_content in ["center", "start", "end"]:
    print("Boxes are horizontally aligned (grid layout)")
elif container_display == "flex" and align_items in ["center", "start", "end"]:
    print("Boxes are horizontally aligned (flex layout)")
else:
    print("Boxes are not horizontally aligned")

# Get the width of the boxes
box1_width = box1.size["width"]
box2_width = box2.size["width"]

# Check if the width of the boxes are equal
if box1_width == box2_width:
    print("Boxes have equal width")
else:
    print("Boxes have different width")

# Close the browser
driver.close()
