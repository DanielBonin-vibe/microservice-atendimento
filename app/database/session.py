import os, psycopg
from dotenv import load_dotenv

load_dotenv()

def conectar():
    return psycopg.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        post=os.getenv('DB_PORT')
    )