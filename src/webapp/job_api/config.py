from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    API_KEY = os.getenv("API_KEY")
    HIVE_HOST = os.getenv("HIVE_HOST")
    HIVE_PORT = int(os.getenv("HIVE_PORT"))
    HIVE_DATABASE = os.getenv("HIVE_DB")
    HIVE_USERNAME = os.getenv("HIVE_USER")