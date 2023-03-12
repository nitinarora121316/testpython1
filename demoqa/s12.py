import subprocess
from selenium import webdriver
import time

# Start the browser and navigate to a website
# browser = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)


driver.get("https://google.com")

time.sleep(2)

# Make changes to a file
# with open("file.txt", "a") as f:
#     f.write("New line of text")

# Add the changes to the staging area using Git
subprocess.run(["git", "add", "."])

# Commit the changes using Git
subprocess.run(["git", "commit", "-m", "Added a new line to file.txt"])

# Push the changes to the remote repository using Git
subprocess.run(["git", "push"])

# Close the browser
driver.quit()
