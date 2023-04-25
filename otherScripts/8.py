from selenium import webdriver
from bs4 import BeautifulSoup

# Set up the driver
driver = webdriver.Chrome()
driver.get("https://ap.bayatree.com")

# Wait for the results page to load
driver.implicitly_wait(5)

# Get the page source
page_source = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Extract the text of all links on the page
links = soup.find_all('a')
for link in links:
    print(link.text)

# Close the driver
driver.quit()
