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
