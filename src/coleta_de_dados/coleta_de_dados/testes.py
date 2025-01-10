import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def get_env(key, default=None):
    value = os.getenv(key)
    return default if value is None else value

db = get_env('DB_HOST')
print(db)