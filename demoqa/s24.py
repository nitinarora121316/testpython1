from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Create an instance of the webdriver
# driver = webdriver.Firefox()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Navigate to a web page
driver.get("https://demoqa.com/automation-practice-form")

# scroll down the page
driver.execute_script("window.scrollBy(0, 500);")



# wait for the dropdown to be visible
dropdown = WebDriverWait(driver, 10).until(
    # EC.visibility_of_element_located((By.XPATH, "//div[@class='css-1hwfws3']"))
    EC.visibility_of_element_located((By.XPATH, "(//div[contains(text(),'Select State')])[1]"))
)

# click on the dropdown to open it
dropdown.click()

# # wait for the NCR option to be visible
# ncr_option = WebDriverWait(driver, 10).until(
#     # EC.visibility_of_element_located((By.XPATH, "//div[@class='css-1x97c6v']/div[contains(text(),'NCR')]"))
#     EC.visibility_of_element_located((By.XPATH, "(//div[@class=' css-1hwfws3'])[1]"))
# )


# wait for the dropdown options to be visible
options_list = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, "//div[@class=' css-11unzgr']/div"))
)


# options_list = WebDriverWait(driver, 10).until(
#     EC.visibility_of_all_elements_located((By.XPATH, "//div[@class=' css-1wa3eu0-placeholder'][1]/following-sibling::div[1]/div"))
# )


# select the 3rd option in the dropdown list
option = options_list[1]
option.click()



time.sleep(2)
# click on the NCR option to select it
# ncr_option.click()
# time.sleep(2)

# close the browser
# driver.quit()