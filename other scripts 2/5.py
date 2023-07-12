from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Replace 'path_to_chromedriver' with the actual path to the ChromeDriver executable
# driver = webdriver.Chrome(executable_path='path_to_chromedriver')
driver = webdriver.Chrome()

try:
    # Open the HTML page with drag and drop elements
    driver.get('http://127.0.0.1:5500/other%20scripts%202/5.html')

    # Locate the drag and drop elements
    drag_element = driver.find_element(By.ID, 'dragContainer')
    drop_element = driver.find_element(By.ID, 'dropContainer')

    # Perform the drag and drop action using ActionChains (manually)
    actions = ActionChains(driver)
    actions.click_and_hold(drag_element).move_to_element(drop_element).release().perform()

    # Optional: You can add a delay to see the changes on the page
    import time
    time.sleep(2)

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
