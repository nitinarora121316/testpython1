from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\asus\Downloads\chromedriver.exe")
# driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get("http://127.0.0.1:5500/other%20scripts%202/8.html#")

time.sleep(3)
# Wait for the download button to be clickable
download_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#download-link"))
)

# Print the text of the download button (optional)
print(download_button.text)

# Click the download button
download_button.click()

print("clicked")

time.sleep(5)


driver.quit()
