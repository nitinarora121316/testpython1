from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# set up Chrome driver
driver = webdriver.Chrome()

# driver = webdriver.Chrome(ChromeDriverManager().install())

# navigate to the webpage
url = 'http://127.0.0.1:5500/chapter4PsR1.html'
driver.get(url)

time.sleep(2)
# execute JavaScript to make the ::after pseudo-element visible
script = "document.styleSheets[0].addRule('footer::after', 'display: block !important')"
driver.execute_script(script)

# find the copyright text element using XPath
copyright_text = driver.find_element(By.XPATH, "//footer[contains(text(), '© infoinfo Ltd. 2023')]")

# check if the text matches what you expect
expected_text = '© infoinfo Ltd. 2023'
assert expected_text in copyright_text.text



# close the browser
driver.quit()
