from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create an instance of the webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Maximize the window
driver.maximize_window()

# Navigate to a web page
driver.get("https://demoqa.com/automation-practice-form")

# Wait for the first name input field to be visible
wait = WebDriverWait(driver, 10)
first_name_field = wait.until(EC.visibility_of_element_located((By.ID, "firstName")))

# Enter a value into the first name field
first_name_field.send_keys("John")

# Close the browser window
driver.quit()
