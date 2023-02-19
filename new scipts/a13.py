from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# start the browser
driver = webdriver.Firefox()

# navigate to the URL
url = "https://google.com"
driver.get(url)

# wait for all elements with the tag "a" to be visible
try:
    WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.TAG_NAME, "a")))
    links = driver.find_elements_by_tag_name("a")
    print("Number of links:", len(links))
except:
    print("No links found or timed out")

# close the browser
driver.quit()
