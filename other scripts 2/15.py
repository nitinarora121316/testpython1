import logging
from selenium import webdriver

# Configure logging
logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Create a Selenium WebDriver instance (replace with your specific WebDriver setup)
driver = webdriver.Chrome(executable_path=r"C:\Users\asus\Downloads\chromedriver.exe")

# Example usage of logging
try:
    driver.get('https://google.comm')
    logging.info('Successfully navigated to "https://example.com"')
except Exception as e:
    logging.error(f'Error: {str(e)}')

# Close the WebDriver
driver.quit()
