from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from webdriver_manager.chrome import ChromeDriverManager

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
    print("href-------", href)
    print("link-------", link.text)

    # Open the link in a new tab
    driver.execute_script("window.open(arguments[0]);", href)

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[1])

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

    # Get the title of the page
    title = driver.title
    print("Page Title:", title)

    # Perform any actions you need on the new tab

    # Close the tab
    driver.close()

    # Switch back to the main tab
    driver.switch_to.window(driver.window_handles[0])

driver.quit()
