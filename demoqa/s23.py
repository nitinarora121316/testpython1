from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Selenium WebDriver instance
# driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.maximize_window()

# Navigate to the webpage with the toggle button and sidebar
driver.get("http://127.0.0.1:5500/index3.html")

time.sleep(2)

# Find the toggle button and sidebar elements
toggle_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "toggle-button"))
)
sidebar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "sidebar"))
)

# Verify that the sidebar is initially hidden
assert sidebar.location['x'] == -200, "Sidebar is not hidden initially"

# Click the toggle button
toggle_button.click()
time.sleep(2)

# Verify that the sidebar is now visible
assert sidebar.location['x'] == 0, "Sidebar is now visible after clicking the toggle button"

# Click the toggle button again
toggle_button.click()
time.sleep(2)

# Verify that the sidebar is hidden again
assert sidebar.location['x'] == -200, "Sidebar is now hidden after clicking the toggle button again"

# Close the browser
driver.quit()
