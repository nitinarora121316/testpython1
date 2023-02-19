from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ap.bayatree.com/media-library/courses")

# Get all images on the page using the By class
images = driver.find_elements(By.TAG_NAME, "img")

# Use a set comprehension to get a set of unique image file types from the images
unique_file_types = {img.get_attribute("src").split(".")[-1] for img in images}

# Print the number of unique file types and the unique file types
print(f"Number of unique image file types: {len(unique_file_types)}")
print(f"Unique image file types: {unique_file_types}")

driver.quit()
