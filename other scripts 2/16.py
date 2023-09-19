import logging
from selenium import webdriver

# Create a custom logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)

# Create a FileHandler to write logs to a file
file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.INFO)

# Define a log format
formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
file_handler.setFormatter(formatter)

# Add the FileHandler to the logger
logger.addHandler(file_handler)

# Create a Selenium WebDriver instance (replace with your specific WebDriver setup)
driver = webdriver.Chrome(executable_path=r"C:\Users\asus\Downloads\chromedriver.exe")

# Example usage of logging
try:
    driver.get('https://google.comm')
    logger.info('Successfully navigated to "https://google.com"')
except Exception as e:
    logger.error(f'Error: {str(e)}')

# Close the WebDriver
driver.quit()
