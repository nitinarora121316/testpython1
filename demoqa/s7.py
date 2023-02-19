from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# set up Chrome driver
driver = webdriver.Chrome()

# navigate to the webpage
url = 'http://127.0.0.1:5500/chapter4PsR1.html'
driver.get(url)

time.sleep(2)
# find the copyright text element using XPath
# copyright_text = driver.find_element(By.XPATH, "//footer[normalize-space()='Footer']")
# copyright_text = driver.find_element(By.XPATH, "//footer/text()[1][contains(., '© infoinfo Ltd. 2023')]")
copyright_text = driver.find_element(By.XPATH, "//footer[contains(., '© infoinfo Ltd. 2023')]")
# find the copyright text element using CSS selector
# copyright_text = driver.find_element(By.CSS_SELECTOR, "footer:contains('© infoinfo Ltd. 2023')")


# check if the text matches what you expect
expected_text = '© infoinfo Ltd. 2023'
# expected_text = 'Footer'
assert expected_text in copyright_text.text

# close the browser
driver.quit()
