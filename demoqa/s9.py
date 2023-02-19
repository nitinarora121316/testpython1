from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# set up Chrome driver
# driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome(ChromeDriverManager().install())

# navigate to the webpage
url = 'http://127.0.0.1:5500/chapter4PsR1.html'
driver.get(url)

time.sleep(2)
# execute JavaScript to get the content of the ::after pseudo-element
script = "return window.getComputedStyle(document.querySelector('footer'), '::after').getPropertyValue('content')"
copyright_text = driver.execute_script(script)

# check if the text matches what you expect
expected_text = '© infoinfo Ltd. 2023'
assert expected_text in copyright_text


# close the browser
driver.quit()
