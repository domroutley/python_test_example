import unittest
from unittest import mock
from example import main as toTestFunc

class TestingClass(unittest.TestCase):

    @mock.patch('example.myRequest')
    def test_dictionary_equal(self, mock_request):
        fakeData = {
            "first_second": [
                {
                    "name": "first",
                    "id": "1234"
                },
                {
                    "name": "second",
                    "id": 1234
                }
            ]
        }
        toTestFunc(1234, "first_second")
        mock_request.assert_called_with(data=fakeData)
