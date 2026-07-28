class APIClient:
    def __init__(self, base_url, access_token):
        self.base_url = base_url
        self.access_token = access_token

    def _get_headers(self):
        return {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

    def send_request(self, endpoint, data=None, method='POST'):
        import requests

        url = f"{self.base_url}/{endpoint}"
        headers = self._get_headers()

        try:
            if method == 'POST':
                response = requests.post(url, json=data, headers=headers)
            elif method == 'GET':
                response = requests.get(url, headers=headers)
            else:
                raise ValueError("Unsupported HTTP method")

            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            self._handle_http_error(http_err, response)
        except requests.exceptions.ConnectionError as conn_err:
            raise ConnectionError(f"Connection error: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            raise TimeoutError(f"Request timed out: {timeout_err}")
        except Exception as err:
            raise Exception(f"An error occurred: {err}")

    def _handle_http_error(self, http_err, response):
        status_code = response.status_code
        if status_code == 400:
            raise ValueError("Bad Request: The server could not understand the request.")
        elif status_code == 401:
            raise PermissionError("Unauthorized: Access token is invalid or expired.")
        elif status_code == 403:
            raise PermissionError("Forbidden: You do not have permission to access this resource.")
        elif status_code == 404:
            raise FileNotFoundError("Not Found: The requested resource could not be found.")
        elif status_code == 500:
            raise Exception("Internal Server Error: The server encountered an error.")
        else:
            raise Exception(f"HTTP error occurred: {http_err}")