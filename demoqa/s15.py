import itertools
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def jumble_string(string):
    words = string.split()
    permutations = itertools.permutations(words)
    return [' '.join(permutation) for permutation in permutations]

# example usage
input_string = "hello how are you"
jumbled_strings = jumble_string(input_string)

# start the web driver and navigate to the page
# driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# driver.get("https://www.google.com")
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(2)

# Find all elements with a specific class
elements = driver.find_elements(By.CLASS_NAME,'form-label')

# Use map to extract the text from each element
element_texts = list(map(lambda element: element.text, elements))

# Print the list of element texts
print(element_texts)

# Define the expected list of element texts
expected_texts = ['Name1', 'Email', 'Mobile(10 Digits)', 'Date of Birth', 'Subjects', 'Hobbies', 'Picture', 'Current Address', 'State and City']

# Verify that the extracted element texts match the expected list
assert element_texts == expected_texts, f"Element texts {element_texts} do not match expected texts {expected_texts}"

# Close the webdriver
driver.quit()