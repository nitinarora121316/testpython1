from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ap.bayatree.com")

# Loop through the list of links and check if each link is working
while True:
    # Get all links on the page using the By class
    links = driver.find_elements(By.TAG_NAME, "a")

    if not links:
        break

    link = links.pop(0)
    try:
        link_url = link.get_attribute("href")
        driver.get(link_url)
        if driver.title:
            print(f"Link {link_url}) is working")
        else:
            print(f"Link {link_url}) is not working")
        driver.back()
    except Exception as e:
        print(f"An error occurred while retrieving link: {e}")

driver.quit()
