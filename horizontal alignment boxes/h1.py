from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Initialize a new browser instance
# driver = webdriver.Chrome(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://ap.bayatree.com")

wait = WebDriverWait(driver, 10)
# search_bar = wait.until(EC.presence_of_element_located((By.ID, 'search-form-control header-search-bar')))
# search_bar.send_keys("selenium python")
time.sleep(5)

# Find the search bar element and enter a query
# search_bar = driver.find_element_by_xpath("//input[@placeholder='Search']")
# search_bar = driver.find_element_by_class_name("search-form-control header-search-bar")
search_bar = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search_bar.send_keys("selenium python")
time.sleep(5)



# Wait for the page to load
driver.implicitly_wait(10)

# Print the title of the page
print(driver.title)

# Close the browser
driver.quit()
