# AI Embedding 26

This project implements a Python API client for interacting with AI embedding services. It is designed to communicate with the Google Gemini Embedding API while providing a clean architecture for authentication, request handling, error management, and embedding generation.


## Features

- Python-based AI embedding client
- Google Gemini Embedding API integration
- REST API communication
- Environment-based configuration using `.env`
- Modular project architecture
- Custom exception handling
- Unit testing with `pytest`


## Project Structure

```
ai-embedding-26
├── src
│   ├── __init__.py
│   ├── client.py
│   ├── config.py
│   ├── exceptions.py
│   ├── models
│   │   ├── __init__.py
│   │   └── embedding.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── request_handler.py
│   └── services
│       ├── __init__.py
│       └── embedding_service.py
├── tests
│   ├── __init__.py
│   ├── test_client.py
│   └── test_services.py
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Configuration

Before running the application, ensure that you have a `.env` file in the root directory with the following variables:

```
SERVER_URL=https://generativelanguage.googleapis.com/v1beta/models/text-embedding-004:embedContent
ACCESS_TOKEN=YOUR_API_KEY
```

## Usage

To use the APIClient, you can create an instance of the class and call its methods to interact with the AI Embedding Server. Here is a simple example:

```python
from src.client import APIClient

client = APIClient()
response = client.send_request(data)
```

## Testing

To run the tests, use the following command:

```
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
