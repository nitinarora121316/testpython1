from selenium import webdriver
from selenium.webdriver.common.by import By

# Create an instance of the webdriver
# driver = webdriver.Firefox()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Navigate to a web page
driver.get("https://demoqa.com/automation-practice-form")

# Find all the elements with the tag name "p"
elements = driver.find_elements(By.TAG_NAME, "label")

# Extract only the elements at odd indices using a list comprehension
# result = [element.text for index, element in enumerate(elements) if index % 2 == 0]
result = [element.text for index, element in enumerate(elements)]

expected_list = ['Name1', 'Email', 'Male', 'Female', 'Other', 'Mobile(10 Digits)', 'Date of Birth', 'Subjects', 'Hobbies', 'Sports', 'Reading', 'Music', 'Picture', 'Select picture', 'Current Address', 'State and City']

if result == expected_list:
    print("The result contains the expected list")
else:
    print("The result does not match the expected list")

# Print the resulting list
print(result)

# Close the browser window
driver.quit()
