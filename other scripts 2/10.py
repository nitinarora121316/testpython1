import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
# import chromedriver_autoinstaller

# Find the Chrome WebDriver version and download the appropriate version of ChromeDriver
# chromedriver_autoinstaller.install()

# # Start Chrome with Selenium
# options = Options()
# options.add_argument("--headless")  # Run Chrome in headless mode (without opening a window)
# driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome(executable_path=r"C:\Users\asus\Downloads\chromedriver.exe")
# driver = webdriver.Firefox()
driver = webdriver.Chrome()




# Define the colors you want to select
colors = ['red', 'green', 'blue']

try:
    # Navigate to the desired location
    # driver.get('http://127.0.0.1:5500/cypress/e2e/1.html')
    driver.get('http://127.0.0.1:5500/other%20scripts%202/10.html')

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'red')))  # Wait for the first radio button to be present

    # Loop through the colors and select the corresponding radio button
    for color in colors:
        radio_button = driver.find_element(By.CSS_SELECTOR, f'input#{color}')
        radio_button.click()
        time.sleep(1)  # Add some delay for demonstration purposes

        # Add any other assertions or actions you want to perform for each color selection

finally:
    # Close the browser
    driver.quit()
