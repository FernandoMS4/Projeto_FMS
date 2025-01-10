import os
from dotenv import load_dotenv, find_dotenv
import mysql.connector

load_dotenv(find_dotenv())

def get_env(key, default=None):
    value = os.getenv(key)
    return default if value is None else value

DB_HOST = get_env('DB_HOST')
DB_USER = get_env('DB_USER')
DB_PASSWORD = get_env('DB_PASSWORD')
DB_PORT = get_env('DB_PORT')
DB_NAME = get_env('DB_NAME')

def verificar_database():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor()
        
        cursor.execute(f"show databases like '{DB_NAME}'")
        result = cursor.fetchone()
        
        if not result:
            # Criar o banco de dados
            cursor.execute(f"CREATE DATABASE {DB_NAME}")
            print(f"Banco de dados '{DB_NAME}' criado com sucesso.")
        else:
            print(f"Banco de dados '{DB_NAME}' já existe.")
        
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Erro ao verificar/criar o banco de dados: {err}")

if __name__ == '__main__':
    print(verificar_database())