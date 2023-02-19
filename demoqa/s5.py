from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Start a webdriver instance
driver = webdriver.Chrome()

# Open the Python shell in the browser
driver.get("https://repl.it/languages/python")

time.sleep(5)

# Find the code input element
code_input = driver.find_element(By.XPATH, "//div[@class='cm-activeLine cm-line']")

# Clear the code input element
try:
    code_input.clear()
    time.sleep(5)
except Exception as e:
    print("Error clearing the code input:", e)

code_input.send_keys("num = int(input('Enter a number: '))\n")
code_input.send_keys("table = [i * num for i in range(1, 11)]\n")
code_input.send_keys("for i in range(1, 11):\n")
code_input.send_keys("    print(f'{num} x {i} = {table[i-1]}')\n")

# Find the run button and click it
run_button = driver.find_element(By.XPATH, "//div[@role='button']")
run_button.click()
time.sleep(5)

# Find the code input element
code_input1 = driver.find_element(By.XPATH, "//textarea[@aria-label='Terminal input']")
code_input1.send_keys("5")
code_input1.send_keys(Keys.RETURN)
time.sleep(5)


wait = WebDriverWait(driver, 20)
output = wait.until(EC.visibility_of_element_located((By.XPATH, "//canvas[@class='xterm-cursor-layer']")))

# wait = WebDriverWait(driver, 20)
# output = wait.until(EC.presence_of_element_located((By.XPATH, "//canvas[@class='xterm-cursor-layer']")))

# wait = WebDriverWait(driver, 10)
# loading_indicator = driver.find_element(By.XPATH, "//div[@class='loading-indicator']")
# wait.until(EC.invisibility_of_element_located(loading_indicator))
# output = driver.find_element(By.XPATH, "//div[@class='xterm-helpers']")



# output = wait.until(EC.visibility_of_element_located((By.XPATH, "//textarea[@class='xterm-helper-textarea']")))
# output = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='xterm-helpers']//textarea")))


# Wait for the output to appear
# output = driver.find_element(By.XPATH, "//div[@class='xterm-helpers']")
print(output.text)
time.sleep(5)
