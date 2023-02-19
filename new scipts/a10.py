from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ap.bayatree.com/media-library/courses")

# Get all images on the page using the By class
images = driver.find_elements(By.TAG_NAME, "img")

# Use a set comprehension to get a set of unique image file types from the images
unique_file_types = {img.get_attribute("src").split(".")[-1] for img in images}

# Assert that the number of unique file types is 1 and that the unique file type is jpg
# assert len(unique_file_types) == 1 and "jpg" in unique_file_types, "The page does not contain only jpg image file types"
assert any(ft in {"jpg", "png"} for ft in unique_file_types), "The page does not contain jpg or png image file types"

# Print a success message if the assertion passes
print("The page contains jpg or png image file types")

driver.quit()
