from selenium import webdriver

# Set up the WebDriver (you should replace 'path_to_chromedriver' with the actual path to your ChromeDriver executable)
driver = webdriver.Chrome(executable_path=r"C:\Users\asus\Downloads\chromedriver.exe")

# Navigate to the URL
url = "https://www.amazon.in"
driver.get(url)

# Take a screenshot and save it to a file
screenshot_file = "amazon_homepage.png"
driver.save_screenshot(screenshot_file)

# Close the WebDriver
driver.quit()

print(f"Screenshot saved as '{screenshot_file}'")
