from selenium import webdriver

class A:
    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        return len(self.lst)

a1 = A([3, 2, 5, 6])
a2 = A([3, 2, 5])
a3 = A([3, 2, 5, 5, 6, "hello"])

# Initialize the webdriver
# driver = webdriver.Firefox()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Navigate to a website to verify the length of the lists
driver.get("http://www.example.com")

# Verify that the length of the list in each A object is as expected
assert len(a1) == 4, f"Expected length 4 but got {len(a1)}"
assert len(a2) == 3, f"Expected length 3 but got {len(a2)}"
assert len(a3) == 6, f"Expected length 6 but got {len(a3)}"

# Close the browser
driver.quit()
