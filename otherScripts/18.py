from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Replace with the path to your chromedriver executable
driver.maximize_window()


# Load the website URL
url = "https://auth0.openai.com/u/login/identifier?state=hKFo2SBwMXVfMzBKQWtSSFRSREpTb0dFTnNIa2FGVC1vXzY2QaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIGJja1hoMWNlRU5ibWlNSjdLZWZ1cGF1MjNKVWU3YWNJo2NpZNkgVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEc"
driver.get(url)

time.sleep(1)

# Find and click the button
buttonLogin = driver.find_element(By.XPATH, "(//button[@class='btn relative btn-primary'])[1]")
buttonLogin.click()
time.sleep(4)

# Wait until the reCAPTCHA checkbox is clickable
checkbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='recaptcha-checkbox-border']"))
)

# Click the checkbox
checkbox.click()

print("hello")
time.sleep(4)

# username = driver.find_element(By.CSS_SELECTOR, "#username")
# username.send_keys("nitin.arora121314@gmail.com")

# buttonContinue = driver.find_element(By.XPATH, "(//button[normalize-space()='Continue'])[1]")
# buttonContinue.click()

# password = driver.find_element(By.CSS_SELECTOR, "#password")
# password.send_keys("gptgpt123@")

# buttonContinue = driver.find_element(By.XPATH, "(//button[normalize-space()='Continue'])[1]")
# buttonContinue.click()

# firstLine = driver.find_element(By.XPATH, "(//div[@class='flex-1 text-ellipsis max-h-5 overflow-hidden break-all relative'])[1]")
# firstLine.click()

time.sleep(1)