from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# set up the web driver
# driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# navigate to a website
driver.get("https://demoqa.com/automation-practice-form")

# find some elements on the page
labels = driver.find_elements(By.TAG_NAME, "label")

# extract text from the label elements
# label_text = []
# for label in labels:
#     label_text.append(label.text)

labels = driver.find_elements(By.TAG_NAME, "label")
label_text = [label.text for label in labels]



# create a DataFrame with the extracted data
data = {'Label Text': label_text}
df = pd.DataFrame(data)

# write the DataFrame to a CSV file
df.to_csv('my_data.csv', index=False)

# close the web driver
driver.quit()
