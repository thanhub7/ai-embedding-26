from src.client import APIClient
from src.exceptions import CustomHTTPError

class EmbeddingService:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def get_embedding(self, text: str):
        try:
            response = self.api_client.send_request("POST", "/embeddings", json={"text": text})
            return response.get("embedding")
        except CustomHTTPError as e:
            print(f"Error occurred: {e}")
            return None

    def batch_get_embeddings(self, texts: list):
        try:
            response = self.api_client.send_request("POST", "/embeddings/batch", json={"texts": texts})
            return response.get("embeddings")
        except CustomHTTPError as e:
            print(f"Error occurred: {e}")
            return None