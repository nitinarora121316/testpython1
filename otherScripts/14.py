import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

# Set up the WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://testautomationpractice.blogspot.com")

# Find and click the button
button = driver.find_element(By.XPATH, "//button[text()='Click Me']")
button.click()

# Add a delay of 2 seconds
time.sleep(2)

# Switch to the alert and accept it
alert = Alert(driver)
# alert.accept()
alert.dismiss()

# Wait for the message to appear on the DOM
time.sleep(2)  # Adjust the delay if necessary

# Retrieve the message from the DOM
# message_element = driver.find_element(By.XPATH, "//p[@id='demo']")
message_element = driver.find_element(By.CSS_SELECTOR, "p#demo")

message = message_element.text

# Print the message
print(message)

# Close the WebDriver
driver.quit()
