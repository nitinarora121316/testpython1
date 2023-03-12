from selenium import webdriver
import time

# Start a new browser session
# driver = webdriver.Chrome()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Navigate to a webpage
# driver.get("http://127.0.0.1:5500/")
driver.get("https://google.com")

# Execute JavaScript code in the browser console
driver.execute_script("""
    console.log("============");
    let called2 = 1;
    function abc1() {
        if (called2) {
            console.log("hello");
            called2--;
        } else {
            console.log("I have been called already");
        }
    }
    abc1();
    abc1();
""")

time.sleep(2)

# Retrieve the logs from the browser console
logs = driver.get_log('browser')
for log in logs:
    print(log)

while True:
    pass

# Close the browser session
# driver.quit()
