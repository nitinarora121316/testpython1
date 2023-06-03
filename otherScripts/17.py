from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Replace with the path to your chromedriver executable
driver.maximize_window()

# Load the website URL
url = "https://ui.vision/demo/webtest/frames/"
driver.get(url)

# Switch to the iframe of Frame 3
frame_3_locator = (By.XPATH, '//frame[@src="frame_3.html"]')
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(frame_3_locator))

# Switch to the iframe within Frame 3
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

# Wait for the radio button to be clickable
radio_button_locator = (By.XPATH, '//label[text()="I am a human"]/input')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(radio_button_locator))

# Click on the radio button
radio_button = driver.find_element(*radio_button_locator)
radio_button.click()
time.sleep(2)

# Switch back to the main content
driver.switch_to.default_content()

# Close the browser
driver.quit()
