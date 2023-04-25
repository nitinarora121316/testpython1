from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the driver
driver = webdriver.Chrome()
driver.get("https://ap.bayatree.com")

# Get the HTML code
# html_code = driver.execute_script("return document.documentElement.outerHTML")
html_code = driver.page_source

# Close the driver
driver.quit()

# Print the HTML code
print(html_code)
