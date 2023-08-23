from XLUtils import XLUtils
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver
driver = webdriver.Chrome(executable_path=r"C:\Users\asus\Downloads\chromedriver.exe")

# Navigate to the OrangeHRM login page
driver.get("https://app.vwo.com/#/login")

if __name__ == "__main__":
    file = "other scripts 2/DataDriven/1.xlsx"  # Replace with your Excel file path
    xlutils = XLUtils(file)
    sheetName = "Sheet1"
    all_data = xlutils.fetchAllData(sheetName)

    for row_num, row_data in enumerate(all_data, start=2):
        username = row_data[0]  # Assuming username is in the first column
        password = row_data[1]  # Assuming password is in the second column

        # Find the username and password input fields and enter your login credentials
        username_field = driver.find_element(By.CSS_SELECTOR, '#login-username')
        username_field.clear()  # Clear the field before entering data
        username_field.send_keys(username)

        password_field = driver.find_element(By.CSS_SELECTOR, '#login-password')
        password_field.clear()  # Clear the field before entering data
        password_field.send_keys(password)

        time.sleep(2)

        # Submit the login form
        login_button = driver.find_element(By.CSS_SELECTOR, '#js-login-btn')
        login_button.click()
        
        time.sleep(2)

        # Add any necessary waiting or error handling here
