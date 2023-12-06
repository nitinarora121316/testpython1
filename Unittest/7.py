import unittest

class TestTextInList(unittest.TestCase):

    def test_text_in_list(self):
        # Sample list for testing
        sample_list = ['Apple', 'Banana', 'Orange', 'Grapes']

        # Text to check for in the list
        text_to_check = 'Orange1'

        # Assert that the text_to_check is present in the list
        self.assertIn(text_to_check, sample_list, f"{text_to_check} not found in the list")

if __name__ == '__main__':
    unittest.main()
