import unittest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

class TestWebDriver(unittest.TestCase):

    def test_executable_path_is_none(self):
        # Set the executable_path to None
        executable_path = None

        # Try to create a WebDriver instance with the specified executable path
        try:
            # driver = webdriver.Chrome(executable_path=executable_path)
            driver = webdriver.Chrome()

            # options = webdriver.ChromeOptions()
            # options.add_experimental_option('excludeSwitches', ['enable-logging'])
            # driver = webdriver.Chrome(options=options)

        except WebDriverException as e:
            # Verify that the exception message contains the expected error
            self.assertIn("executable needs to be in PATH", str(e))

        else:
            # If no exception is raised, fail the test
            self.fail("Expected exception not raised")

if __name__ == '__main__':
    unittest.main()
