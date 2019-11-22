import unittest
from unittest import mock
from example import main as toTestFunc

class TestingClass(unittest.TestCase):

    @mock.patch('sys.stdout')
    @mock.patch('example.myRequest')
    def test_dictionary_equal_true(self, mock_request, mock_stdout):
        num = 1234
        fakeData = {
            "first_second": [
                {
                    "name": "first",
                    "id": num
                },
                {
                    "name": "second",
                    "id": str(num)
                }
            ]
        }
        toTestFunc(num, "first_second", True)
        mock_request.assert_called_with(data=fakeData)

    @mock.patch('sys.stdout')
    @mock.patch('example.myRequest')
    def test_dictionary_equal_false(self, mock_request, mock_stdout):
        num = 1234
        fakeData = {
            "first_second": [
                {
                    "name": "first",
                    "id": str(num)
                },
                {
                    "name": "second",
                    "id": num
                }
            ]
        }
        toTestFunc(num, "first_second", False)
        mock_request.assert_called_with(data=fakeData)
