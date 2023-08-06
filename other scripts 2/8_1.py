from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

firefox_options = Options()
firefox_options.set_preference("browser.download.folderList", 2)
firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
firefox_options.set_preference("browser.download.dir", r"C:\Users\asus\Desktop\MA script")
firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

# Uncomment the following line if you want to see the Firefox browser in action
# firefox_options.headless = False

# Initialize the Firefox webdriver
# driver = webdriver.Firefox(executable_path=r"C:\Users\asus\Downloads\geckodriver.exe", options=firefox_options)
driver = webdriver.Firefox(options=firefox_options)

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

# You can add additional code here to wait for the file to finish downloading if needed

# Close the browser
driver.quit()
