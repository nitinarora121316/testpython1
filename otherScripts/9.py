from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a new instance of the Chrome driver
# driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)



# Navigate to the web page that contains the list
driver.get("https://yahoo.com")

print(driver.title)

time.sleep(2)

driver.get("https://google.com")
time.sleep(2)
print(driver.title)

driver.back()
time.sleep(2)
print(driver.title)

driver.forward()
time.sleep(2)
print(driver.title)

driver.back()
time.sleep(2)
print(driver.title)








