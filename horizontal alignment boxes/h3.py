from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

# Create a new instance of the Firefox driver
# driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Navigate to google.com
driver.get("https://www.google.com")

# Find the search box element by its name
search_box = driver.find_element(By.NAME, 'q')

# Enter a search query
search_box.send_keys("Selenium automation with Python")

# Find the search button element by its name
search_button = driver.find_element(By.NAME, 'btnK')

# Click the search button
search_button.click()

# Close the browser
driver.quit()
