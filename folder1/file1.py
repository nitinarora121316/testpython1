# file1.py in folder1

import unittest

class YourTestCase(unittest.TestCase):
    def test_test1(self):
        self.assertEqual(1 + 1, 2)

    def test_test2(self):
        self.assertTrue(True)  # Add your test logic here



if __name__ == "__main__":
    unittest.main()
