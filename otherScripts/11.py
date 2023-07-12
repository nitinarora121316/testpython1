from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

# Create an instance of the webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

url = "https://ap.bayatree.com"
driver.get(url)

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

for link in links:
    href = link.get_attribute("href")
    print("href-------",href)
    print("link-------",link.text)

driver.quit()