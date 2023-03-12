from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the webdriver and navigate to the URL
driver = webdriver.Chrome()
driver.get('https://google.com')

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='q']")))

# Get all links on the page using a lambda function with the find_elements method
links = driver.find_elements(By.XPATH, "//a")
hrefs = list(map(lambda link: link.get_attribute("href"), links))

# Print all the links
for href in hrefs:
    print(href)

# Close the webdriver
driver.quit()
