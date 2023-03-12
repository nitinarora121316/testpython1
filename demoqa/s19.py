from flask import Flask, render_template
from selenium import webdriver

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    # Start the Chrome browser with Selenium
    # driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.com')
    
    # Find the page title using Selenium
    title = driver.title
    
    # Close the browser window
    driver.quit()

    # Render the home.html template with the page title
    return render_template('home1.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)
