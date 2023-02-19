from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

# Start a webdriver instance
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://google.co.in")

# Get all links on the page
links = driver.find_elements(By.TAG_NAME, "a")

# Check the status code of each link
for link in links:
    try:
        # Wait for the element to be clickable
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.TAG_NAME, "a"))
        )
        # Get the link URL
        url = link.get_attribute("href")
        # Send a GET request to the URL
        response = requests.get(url)
        # Check the status code of the response
        if response.status_code != 200:
            print(f"Link '{url}' returned status code {response.status_code}")
    except:
        print(f"Unable to access link '{url}'")

# Quit the webdriver instance
driver.quit()
