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
driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(2)

# find the text field and fill it in with a jumbled string
text_field = driver.find_element(By.XPATH,"//input[@title='Search']")
for jumbled_string in jumbled_strings:
    text_field.clear()
    text_field.send_keys(jumbled_string)
    text_field.send_keys(Keys.RETURN)
    time.sleep(1)
    driver.back()
    time.sleep(2)
