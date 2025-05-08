from pyhive import hive
from dotenv import load_dotenv
import os

load_dotenv()

HIVE_HOST = os.getenv('HIVE_HOST')
HIVE_PORT = int(os.getenv('HIVE_PORT'))
HIVE_USER = os.getenv('HIVE_USER')
HIVE_DB = os.getenv('HIVE_DB')

# Tạo kết nối tới Hive
def get_hive_connection():
    conn = hive.Connection(
        host=HIVE_HOST,
        port=HIVE_PORT,
        username=HIVE_USER,
        database=HIVE_DB
    )
    return conn
