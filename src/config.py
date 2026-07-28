import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SERVER_URL = os.getenv("SERVER_URL")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

    @staticmethod
    def validate():
        if not Config.SERVER_URL:
            raise ValueError("SERVER_URL is not set in the environment variables.")
        if not Config.ACCESS_TOKEN:
            raise ValueError("ACCESS_TOKEN is not set in the environment variables.")