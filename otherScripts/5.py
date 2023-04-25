from selenium import webdriver

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Navigate to Google's homepage
driver.get("https://www.google.com")

# Get the page title and print it to the console
title = driver.title
print(title)

# Close the browser
driver.quit()
