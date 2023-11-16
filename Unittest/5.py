import unittest
from selenium import webdriver

class TestDriver(unittest.TestCase):

    def test_driver_none(self):
        # Assuming you have a function/method that returns the driver
        driver = webdriver.Chrome()  # Replace with your function/method

        # Use assertIsNone to check if the driver is None
        self.assertIsN  otNone(driver, "The driver is not None")


if __name__ == "__main__":
    unittest.main()