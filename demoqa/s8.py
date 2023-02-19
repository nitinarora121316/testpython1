from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# set up Chrome driver
driver = webdriver.Chrome()

# navigate to the webpage
url = 'http://127.0.0.1:5500/chapter4PsR1.html'
driver.get(url)

time.sleep(2)

# add a hidden span element inside the footer element
driver.execute_script("var element = document.createElement('span'); element.style.display = 'none'; element.textContent = '© infoinfo Ltd. 2023'; document.getElementsByTagName('footer')[0].appendChild(element);")

# find the copyright text element using CSS selector
copyright_text = driver.find_element(By.CSS_SELECTOR, "footer span")
print("=======")

print(copyright_text.text)

print("=======")
# check if the text matches what you expect
expected_text = '© infoinfo Ltd. 2023'
assert expected_text in copyright_text.text

# close the browser
driver.quit()


