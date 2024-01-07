import unittest
from unittest.mock import patch
from io import StringIO

class TestMyCode(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_function(self, mock_stdout):
        x = 5

        def create(y: int):
            print(y)

        create(1234)

        # Assert that the output matches the expected output
        self.assertEqual(mock_stdout.getvalue().strip(), '1234')

    def test_main_code(self):
        x = 5
        def create(y: int):
            print(y)

        create(1234)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Capture the output of the print statement
            print("Hello world")

            # Assert that the output matches the expected output
            self.assertEqual(mock_stdout.getvalue().strip(), 'Hello world')

if __name__ == '__main__':
    unittest.main()
