import unittest
from unittest import mock

from requests.exceptions import HTTPError

from url_manager import get, add, delete, list_all


class MockResponse(object):
    def __init__(self, json_data, status_code, status_error=None):
        self.json_data = json_data
        self.status_code = status_code
        self.text = "{'hello': 'world'}"
        self.status_error = status_error

    def json(self):
        return self.json_data

    def raise_for_status(self):
        # Should only need to support a good response
        # but kind of made it easy to implement it in
        # a half baked way.
        if self.status_code != 200:
            raise HTTPError("Cannot return your request.")


class TestUrlManager(unittest.TestCase):

    def setUp(self):
        self.header = {'Authorization': "token 123"}
        self.redirect_list = [
            {
                "code": "value1",
                "destination": "http://www.a.b.c/",
                "visits": 0
            },
            {
                "code": "value2",
                "destination": "http://www.a.b.c/2",
                "visits": 0
            }
        ]

    @mock.patch('url_manager.requests.get')
    @mock.patch('url_manager.input')
    def test_get(self, mock_input, mock_get):

        mock_input.return_value = "test"
        mock_response = MockResponse(self.redirect_list[0], 200)
        mock_get.return_value = mock_response

        try:
            get(self.header)
        except Exception as e:
            self.fail(f"Failed due to {e}")

    @mock.patch('url_manager.requests.get')
    @mock.patch('url_manager.input')
    def test_get_fail(self, mock_input, mock_get):

        status_code = 404
        success = False

        mock_input.return_value = "test"
        mock_response = MockResponse(None, status_code)
        mock_get.return_value = mock_response

        try:
            get(self.header)
        except HTTPError:
            success = True

        self.assertTrue(success, f"status code {status_code} did not raise exception")

    @mock.patch('url_manager.requests.post')
    @mock.patch('url_manager.input')
    def test_add(self, mock_input, mock_post):
        mock_input.return_value = "test"
        mock_response = MockResponse(self.redirect_list[0], 200)
        mock_post.return_value = mock_response

        try:
            add(self.header)
        except Exception as e:
            self.fail(f"Failed due to {e}")

    @mock.patch('url_manager.requests.delete')
    @mock.patch('url_manager.input')
    def test_delete(self, mock_input, mock_delete):
        mock_input.return_value = "test"
        mock_response = MockResponse(self.redirect_list[0], 200)
        mock_delete.return_value = mock_response

        try:
            delete(self.header)
        except Exception as e:
            self.fail(f"Failed due to {e}")

    @mock.patch('url_manager.requests.get')
    @mock.patch('url_manager.input')
    def test_list_all(self, mock_input, mock_get):
        mock_input.return_value = "test"
        mock_response = MockResponse({"results": self.redirect_list}, 200)
        mock_get.return_value = mock_response

        try:
            list_all(self.header)
        except Exception as e:
            self.fail(f"Failed due to {e}")


if __name__ == "__main__":
    unittest.main()
