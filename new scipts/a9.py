from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ap.bayatree.com/phonics/courses")

# Get all links on the page using the By class
links = driver.find_elements(By.TAG_NAME, "a")

# Use a list comprehension to check if each link is working
working_links = [link for link in links if driver.get(link.get_attribute("href")) == link.get_attribute("href")]

# Print the number of working links
print(f"Number of working links: {len(working_links)}")

driver.quit()
