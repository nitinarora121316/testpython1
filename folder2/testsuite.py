# testsuite.py in folder2

import sys
sys.path.append('e:/PythonSelenium')  # Add the absolute path to the parent directory

from folder1.file1 import YourTestCase as TestCase1 
from folder1.file2 import YourTestCase as TestCase2
import unittest

if __name__ == "__main__":
    # Create test suites
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)

    # Combine the test suites into a single test suite
    all_tests = unittest.TestSuite([suite1, suite2])

    # Create a test runner
    runner = unittest.TextTestRunner()

    # Run the tests
    result = runner.run(all_tests)
