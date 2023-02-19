from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start a webdriver instance
driver = webdriver.Chrome()

# Open the Python shell in the browser
driver.get("https://repl.it/languages/python")

# Find the code input element and enter the code
code_input = driver.find_element(By.XPATH, "//div[@class='cm-scroller']")
code_input.clear()
time.sleep(5)
# code_input.send_keys("num = int(input('Enter a number: '))\n")
# code_input.send_keys("table = [i * num for i in range(1, 11)]\n")
# code_input.send_keys("for i in range(1, 11):\n")
# code_input.send_keys("    print(f'{num} x {i} = {table[i-1]}')\n")

# # Find the run button and click it
# run_button = driver.find_element(By.XPATH, "//div[@role='button']")
# run_button.click()

# # Wait for the output to appear
# output = driver.find_element(By.XPATH, "//canvas[@class='xterm-cursor-layer']")
# print(output.text)

# # Close the webdriver instance
# driver.quit()
