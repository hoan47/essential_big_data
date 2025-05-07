from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    API_KEY = os.getenv("API_KEY")
    # Cấu hình Hive (dùng sau này)
    HIVE_HOST = os.getenv("HIVE_HOST", "localhost")
    HIVE_PORT = os.getenv("HIVE_PORT", 10000)
    HIVE_DATABASE = os.getenv("HIVE_DATABASE", "default")
    HIVE_USERNAME = os.getenv("HIVE_USERNAME", None)
    HIVE_PASSWORD = os.getenv("HIVE_PASSWORD", None)