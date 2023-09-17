from selenium import webdriver

# Set up the WebDriver (you should replace 'path_to_chromedriver' with the actual path to your ChromeDriver executable)
driver = webdriver.Chrome(executable_path=r"C:\Users\asus\Downloads\chromedriver.exe")

# Navigate to the URL
url = "https://www.amazon.in"
driver.get(url)

# Capture all cookies
cookies = driver.get_cookies()

print(len(cookies))

# Print all the cookies
for cookie in cookies:
    print(f"Name: {cookie['name']}")
    print(f"Value: {cookie['value']}")
    print(f"Domain: {cookie['domain']}")
    print(f"Path: {cookie['path']}")
    print(f"Expires: {cookie['expiry']}")
    print(f"Secure: {cookie['secure']}")
    print(f"HttpOnly: {cookie['httpOnly']}")
    print("\n")

# Close the WebDriver
driver.quit()
import logging
from selenium import webdriver

# Configure logging
logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Create a Selenium WebDriver instance (replace with your specific WebDriver setup)
driver = webdriver.Chrome()

# Example usage of logging
try:
    driver.get('https://google.com')
    logging.info('Successfully navigated to "https://example.com"')
except Exception as e:
    logging.error(f'Error: {str(e)}')

# Close the WebDriver
driver.quit()
