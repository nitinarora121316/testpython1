from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Wait for the login process to complete
driver.implicitly_wait(10)  # Wait for 10 seconds for the login to complete, adjust as needed


# Find the username and password input fields and enter your login credentials
username_field = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
username_field.send_keys("Admin")

password_field = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
password_field.send_keys("admin123")

# Submit the login form
login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
login_button.click()

# Wait for the login process to complete
driver.implicitly_wait(10)  # Wait for 10 seconds for the login to complete, adjust as needed

# Perform any further actions on the logged-in page if desired.

# Close the WebDriver
driver.quit()
