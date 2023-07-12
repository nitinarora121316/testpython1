from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Replace 'path_to_chromedriver' with the actual path to the ChromeDriver executable
# driver = webdriver.Chrome(executable_path='path_to_chromedriver')
driver = webdriver.Chrome()

try:
    # Open the HTML page with drag and drop elements
    driver.get('http://127.0.0.1:5500/other%20scripts%202/5.html')

    # Locate the drag and drop elements
    drag_element = driver.find_element(By.ID, 'dragContainer')
    drop_element = driver.find_element(By.ID, 'dropContainer')

    # Perform the drag and drop action using JavaScript
    js_script = """
        const dragElement = arguments[0];
        const dropElement = arguments[1];

        const dragEvent = new DragEvent('dragstart', { dataTransfer: new DataTransfer() });
        dragElement.dispatchEvent(dragEvent);

        const dropEvent = new DragEvent('drop');
        dropElement.dispatchEvent(dropEvent);
    """

    driver.execute_script(js_script, drag_element, drop_element)

    # Optional: You can add a delay to see the changes on the page
    import time
    time.sleep(8)

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
