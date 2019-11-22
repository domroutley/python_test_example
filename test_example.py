import unittest
from unittest import mock
from example import main as toTestFunc

class TestingClass(unittest.TestCase):

    @mock.patch('example.myRequest')
    def test_dictionary_equal(self, mock_request):
        fakeData = {
            "fields": {
                "fake_custom": [
                    {
                        "id": "1234"
                    },
                    {
                        "id": "fake_project_lead"
                    }
                ]
            }
        }
        fakeData2 = {
            "fields": {
                "fake_custom": [
                    {
                        "id": "fake_project_lead"
                    },
                    {
                        "id": "1234"
                    }
                ]
            }
        }
        toTestFunc(num="1234", name="fake_project_lead")
        mock_request.assert_called_with(data=fakeData2)
