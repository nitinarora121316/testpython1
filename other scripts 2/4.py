from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# Replace 'path_to_chrome_driver' with the actual path to your Chrome driver executable
driver = webdriver.Chrome(executable_path='path_to_chrome_driver')

try:
    driver.get("http://127.0.0.1:5500/other%20scripts%202/4.html")

    button = driver.find_element(By.CLASS_NAME, "right-click-button")

    # Perform a right-click on the button
    actions = ActionChains(driver)
    actions.context_click(button).perform()

    # Wait for the context menu to appear
    time.sleep(1)

    # Assert whether the "Edit" option is present in the context menu
    options = driver.find_elements(By.CLASS_NAME, "options")[0].find_elements(By.TAG_NAME, "a")
    option_texts = [option.text for option in options]
    assert "Edit" in option_texts, "Edit option not found in the context menu"

finally:
    driver.quit()
