from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

# Create an instance of the webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Navigate to a web page
driver.get("http://127.0.0.1:5500/demoqa/templates/dropdown.html")

# Wait for the dropdown element to be visible
dropdown = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "my-select"))
)

# Create a Select object for the dropdown
select = Select(dropdown)

# Select all options one by one
for index in range(len(select.options)):
    print(index.text)
    select.select_by_index(index)
    time.sleep(2)

# Close the browser
driver.quit()
