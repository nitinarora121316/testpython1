from selenium import webdriver
from selenium.webdriver.common.by import By

# Import the Keys class
from selenium.webdriver.common.keys import Keys

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Navigate to Google's homepage
driver.get("https://www.google.com")

# Find the search box element and type a query
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("Python programming" + Keys.RETURN)

# Wait for the results page to load
driver.implicitly_wait(5)

# Get the page title and print it to the console
title = driver.title
print(title)

# Close the browser
driver.quit()
