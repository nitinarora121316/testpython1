import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Replace with the path to your chromedriver executable
driver.maximize_window()

# Load the website URL
url = "http://127.0.0.1:5500/otherScripts/2.html"
driver.get(url)
print(driver.current_url)

# Locate all table rows (tr elements)
table_rows = driver.find_elements(By.XPATH, "//tr")

# Get the number of rows and columns
num_rows = len(table_rows)
num_columns = 0

# Iterate over the table rows and count the maximum number of columns
for row in table_rows:
    cells = row.find_elements(By.XPATH, ".//td")
    num_columns = max(num_columns, len(cells))

# Print the number of rows and columns
print("Number of rows:", num_rows)
print("Number of columns:", num_columns)

# Close the browser
driver.quit()
