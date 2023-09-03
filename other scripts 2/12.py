from selenium import webdriver

# Set up the WebDriver (you should replace 'path_to_chromedriver' with the actual path to your ChromeDriver executable)
driver = webdriver.Chrome(executable_path=r"C:\Users\asus\Downloads\chromedriver.exe")

# Navigate to the URL
url = "https://www.amazon.in"
driver.get(url)

# Define your own cookies
custom_cookies = [
    {'name': 'my_cookie1', 'value': 'value1', 'domain': '.amazon.in', 'path': '/', 'secure': False},
    {'name': 'my_cookie2', 'value': 'value2', 'domain': '.amazon.in', 'path': '/', 'secure': False},
]

# Add your own cookies
for cookie in custom_cookies:
    driver.add_cookie(cookie)

# Capture all cookies (including the ones you added)
all_cookies = driver.get_cookies()

# Print all the cookies
for cookie in all_cookies:
    print(f"Name: {cookie['name']}")
    print(f"Value: {cookie['value']}")
    print(f"Domain: {cookie['domain']}")
    print(f"Path: {cookie['path']}")
    
    # Check if the 'expiry' key exists before trying to access it
    if 'expiry' in cookie:
        print(f"Expires: {cookie['expiry']}")
    else:
        print("Expires: None")
    
    print(f"Secure: {cookie.get('secure', 'None')}")
    print(f"HttpOnly: {cookie.get('httpOnly', 'None')}")
    print("\n")

# Close the WebDriver
driver.quit()
