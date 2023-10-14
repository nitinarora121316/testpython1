import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class ColorSelectionTest(unittest.TestCase):
    def setUp(self):
        # Set up the Selenium WebDriver
        # options = Options()
        # options.headless = False  # Set to True if you want to run tests in headless mode
        # self.driver = webdriver.Chrome(options=options)
        # self.driver.maximize_window()
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\asus\Downloads\chromedriver.exe")

    def test_color_selection(self):
        # Define the colors you want to select
        colors = ['red', 'green', 'blue']

        try:
            # Navigate to the desired location
            self.driver.get('http://127.0.0.1:5500/other%20scripts%202/10.html')

            # Wait for the page to load
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.ID, 'red')))  # Wait for the first radio button to be present

            # Loop through the colors and select the corresponding radio button
            for color in colors:
                radio_button = self.driver.find_element(By.CSS_SELECTOR, f'input#{color}')
                radio_button.click()
                time.sleep(1)  # Add some delay for demonstration purposes

                # Add any other assertions or actions you want to perform for each color selection

        finally:
            pass  # You can add cleanup code here if needed

    def test_file_upload(self):
        # Navigate to the file upload page
        self.driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")

        file_path = r"C:\Users\asus\Desktop\1 Copy.txt"  # Replace with the actual file path
        file_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='upfile']")
        file_input.send_keys(file_path)

        # Optionally, perform additional actions before submitting the form or continuing with the upload process

        upload_button = self.driver.find_element(By.CSS_SELECTOR, "input[value='Press']")
        upload_button.click()

        time.sleep(3)

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
