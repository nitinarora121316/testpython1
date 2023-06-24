import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Replace with the path to your chromedriver executable
driver.maximize_window()

# Load the website URL
url = "http://127.0.0.1:5500/otherScripts/2.html"
driver.get(url)
print(driver.current_url)

# Locate all table rows (tr elements)
table_rows = driver.find_elements(By.XPATH, "//tr")

# Create an empty list to store the data
data = []

# Iterate over the table rows and extract the text of each cell
for row in table_rows:
    cells = row.find_elements(By.XPATH, ".//td")
    row_data = [cell.text for cell in cells]  
    data.append(row_data)

# Close the browser
driver.quit()

# Create a pandas DataFrame with the extracted data and column headings
df = pd.DataFrame(data, columns=["FirstName", "LastName", "Email"])

# Print the DataFrame
print(df)
