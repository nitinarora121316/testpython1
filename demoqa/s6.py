from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create a new Chrome browser instance
browser = webdriver.Chrome()

# Navigate to a blank page
browser.get("about:blank")

# Get the body element of the page
body = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Get the number from the user
number = input("Enter a number: ")

# Create a table element
table = browser.execute_script("return document.createElement('table')")

# Loop through the numbers and create the rows
for i in range(1, 13):
    result = int(number) * i
    row = browser.execute_script("return document.createElement('tr')")
    if i % 2 == 0:
        # Use green color for even rows
        color = "green"
    else:
        # Use red color for odd rows
        color = "red"
    output = f"{number} x {i} = <span style='color: {color}'>{result}</span>"
    cell = browser.execute_script(f"return document.createElement('td');")
    cell.innerHTML = output
    row.appendChild(cell)
    table.appendChild(row)

# Add the table to the body of the page
body.appendChild(table)

# Save the page as an HTML file
with open("multiplication_table11.html", "w") as file:
    file.write(browser.page_source)

# Close the browser
browser.quit()
