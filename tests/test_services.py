import unittest
from unittest.mock import patch, MagicMock
from src.services.embedding_service import EmbeddingService
from src.client import APIClient
from src.exceptions import CustomHTTPError

class TestEmbeddingService(unittest.TestCase):

    @patch.object(APIClient, 'send_request')
    def test_get_embedding_success(self, mock_send_request):
        mock_response = MagicMock()
        mock_response.json.return_value = {'embedding': [0.1, 0.2, 0.3]}
        mock_send_request.return_value = mock_response
        
        service = EmbeddingService()
        result = service.get_embedding("test input")
        
        self.assertEqual(result, [0.1, 0.2, 0.3])
        mock_send_request.assert_called_once_with("POST", "/embeddings", json={"input": "test input"})

    @patch.object(APIClient, 'send_request')
    def test_get_embedding_failure(self, mock_send_request):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {'error': 'Bad Request'}
        mock_send_request.return_value = mock_response
        
        service = EmbeddingService()
        
        with self.assertRaises(CustomHTTPError) as context:
            service.get_embedding("test input")
        
        self.assertEqual(str(context.exception), 'Error 400: Bad Request')
        mock_send_request.assert_called_once_with("POST", "/embeddings", json={"input": "test input"})

if __name__ == '__main__':
    unittest.main()