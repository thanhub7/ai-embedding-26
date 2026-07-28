import unittest
from unittest.mock import patch, MagicMock
from src.client import APIClient
from src.exceptions import HTTPError

class TestAPIClient(unittest.TestCase):

    @patch('src.client.requests.post')
    def test_send_request_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': 'embedding_data'}
        mock_post.return_value = mock_response

        client = APIClient()
        response = client.send_request('test_endpoint', {'input': 'test_data'})

        self.assertEqual(response, {'data': 'embedding_data'})
        mock_post.assert_called_once_with('test_endpoint', json={'input': 'test_data'})

    @patch('src.client.requests.post')
    def test_send_request_http_error(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {'error': 'Bad Request'}
        mock_post.return_value = mock_response

        client = APIClient()

        with self.assertRaises(HTTPError):
            client.send_request('test_endpoint', {'input': 'test_data'})

    @patch('src.client.requests.post')
    def test_send_request_connection_error(self, mock_post):
        mock_post.side_effect = ConnectionError("Failed to connect")

        client = APIClient()

        with self.assertRaises(ConnectionError):
            client.send_request('test_endpoint', {'input': 'test_data'})

if __name__ == '__main__':
    unittest.main()