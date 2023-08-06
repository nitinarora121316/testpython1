from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()  # Replace with the path to your webdriver executable
driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")  # Replace with the URL of the webpage

file_path = r"C:\Users\asus\Desktop\1 Copy.txt"  # Replace with the actual file path
file_input = driver.find_element(By.CSS_SELECTOR, "input[name='upfile']")  # Replace "fileInput" with the actual ID of the file input element
file_input.send_keys(file_path)

# Optionally, perform additional actions before submitting the form or continuing with the upload process

upload_button = driver.find_element(By.CSS_SELECTOR, "input[value='Press']")  # Replace "uploadButton" with the actual ID of the upload button or form element
upload_button.click()  # Or use any other appropriate action to initiate the file upload``

time.sleep(3)

driver.quit()
