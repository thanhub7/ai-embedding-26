import requests
from requests.exceptions import RequestException
from src.exceptions import (
    ConnectionErrorException,
    TimeoutException,
    HTTPErrorException,
)

def set_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

def handle_response(response):
    if response.status_code == 200:
        return response.json()
    elif response.status_code in {400, 401, 403, 404, 500}:
        raise HTTPErrorException(f"HTTP Error: {response.status_code} - {response.text}")
    else:
        raise HTTPErrorException(f"Unexpected Error: {response.status_code} - {response.text}")

def make_request(method, url, token, data=None, timeout=10):
    headers = set_headers(token)
    try:
        if method.lower() == 'get':
            response = requests.get(url, headers=headers, timeout=timeout)
        elif method.lower() == 'post':
            response = requests.post(url, headers=headers, json=data, timeout=timeout)
        else:
            raise ValueError("Unsupported HTTP method: {}".format(method))
        
        return handle_response(response)
    except requests.ConnectionError:
        raise ConnectionErrorException("Failed to connect to the server.")
    except requests.Timeout:
        raise TimeoutException("The request timed out.")
    except RequestException as e:
        raise HTTPErrorException(f"An error occurred: {str(e)}")