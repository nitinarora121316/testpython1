from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the webdriver
# driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)




# Navigate to the webpage
# driver.get("http://127.0.0.1:5500/min-max-height-widthR1.html")
driver.get("https://ap.bayatree.com/reading/interactivity/level:1/section:20/lesson:lesson1/activity:4")

# Find the container element
# container = driver.find_element(By.CLASS_NAME, "container")
container = driver.find_element(By.CLASS_NAME, "phonicsMain")

# Get the minimum and maximum height and width
min_height = container.value_of_css_property("min-height")
max_height = container.value_of_css_property("max-height")
min_width = container.value_of_css_property("min-width")
max_width = container.value_of_css_property("max-width")

# Use the retrieved height values to simulate different screen sizes and take screenshots
driver.set_window_size(int(min_width.replace("px", "")), int(min_height.replace("px", "")))
driver.save_screenshot("min_height.png")

print(int(min_width.replace("px", "")))
print(int(min_height.replace("px", "")))
driver.set_window_size(int(max_width.replace("px", "")), int(max_height.replace("px", "")))
print(int(max_width.replace("px", "")))
print(int(max_height.replace("px", "")))
driver.save_screenshot("max_height.png")

# Close the webdriver
driver.quit()
