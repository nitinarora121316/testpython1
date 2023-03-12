from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Navigate to the webpage
driver.get("https://ap.bayatree.com/reading/interactivity/level:1/section:20/lesson:lesson1/activity:4")

# Find the container element
container = driver.find_element(By.CLASS_NAME, "phonicsMain")

# Get the viewport height
viewport_height = driver.execute_script("return window.innerHeight;")
print(viewport_height)

# Get the minimum height in pixels
min_height_percent = container.value_of_css_property("min-height").replace("%", "")
min_height_pixels = int(viewport_height * int(min_height_percent) / 100)
print(min_height_percent)
print(min_height_pixels)

# Use the retrieved height values to simulate different screen sizes and take screenshots
driver.set_window_size(min_height_pixels, viewport_height)
driver.save_screenshot("min_height.png")

max_height_percent = container.value_of_css_property("max-height").replace("%", "")
max_height_pixels = int(viewport_height * int(max_height_percent) / 100)

driver.set_window_size(max_height_pixels, viewport_height)
driver.save_screenshot("max_height.png")

# Close the webdriver
driver.quit()
