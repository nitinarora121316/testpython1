from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Replace with the path to your chromedriver executable
driver.maximize_window()

# Load the website URL
url = "http://demo.automationtesting.in/Windows.html"
driver.get(url)
print(driver.current_url)

button = driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']")
button.click()

time.sleep(2)

print(driver.current_window_handle)
print(driver.current_url)

time.sleep(2)

# Get all window handles
window_handles = driver.window_handles

# Loop over each window handle
for handle in window_handles:
    driver.switch_to.window(handle)
    if "Selenium logo green" in driver.title:
        driver.close()
        time.sleep(2)

# Switch back to the main window
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)

print(driver.current_window_handle)
print(driver.current_url)


# Close the main window
driver.quit()
