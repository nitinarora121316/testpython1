import logging
from selenium import webdriver

# Set up logging
logging.basicConfig(filename='selenium_log.log', level=logging.INFO)  # Change log level as needed

# Create a logger
logger = logging.getLogger(__name__)

# Set up the WebDriver (you should replace 'path_to_chromedriver' with the actual path to your ChromeDriver executable)
driver = webdriver.Chrome(executable_path=r"C:\Users\asus\Downloads\chromedriver.exe")

# Navigate to the URL
url = "https://www.amazon.in"
driver.get(url)

# Take a screenshot and save it to a file
screenshot_file = "amazon_homepage.png"
try:
    driver.save_screenshot(screenshot_file)
    logger.info(f"Screenshot saved as '{screenshot_file}'")
except Exception as e:
    logger.error(f"Failed to save screenshot: {str(e)}")

# Close the WebDriver
driver.quit()
