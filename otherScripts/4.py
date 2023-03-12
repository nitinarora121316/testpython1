import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up Chrome driver and navigate to Gmail login page
driver = webdriver.Firefox()
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)

driver.get("https://mail.google.com")
# driver.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")

time.sleep(5)
# loginGoogle = driver.find_element(By.XPATH,"//button[normalize-space()='Log in with Google']")
# loginGoogle.click()

time.sleep(5)


# Enter email address and click "Next"
email_input = driver.find_element(By.XPATH,"//input[@type='email']")
email_input.send_keys("nitashavig00@gmail.com")
email_input.send_keys(Keys.RETURN)
time.sleep(3)