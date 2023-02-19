from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize a new browser instance
# driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Navigate to a website
driver.get("https://www.amazon.in")

# Find the search bar element and enter a query
search_bar = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
time.sleep(2)
search_bar.send_keys("Python Programming Books")

# Find the search button and click it
search_button = driver.find_element(By.XPATH, "//input[@value='Go']")
search_button.click()

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "s-result-count")))

# Print the title of the page
print(driver.title)

# Get the list of books
books = driver.find_elements(By.XPATH, "//div[@data-index]")

# Print the names and prices of the books
for book in books:
    title = book.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']").text
    price = book.find_element(By.XPATH, ".//span[@class='a-price']/span[@class='a-offscreen']").text
    print(f'{title} - {price}')

# Close the browser
driver.quit()
