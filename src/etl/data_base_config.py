from sqlmodel import  Field,SQLModel,Session,create_engine
from typing import Optional
import mysql.connector
import os
from dotenv import load_dotenv, find_dotenv

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
            cursor.execute(f"CREATE DATABASE {DB_NAME}")
            print(f"Banco de dados '{DB_NAME}' criado com sucesso.")
        else:
            print(f"Banco de dados '{DB_NAME}' já existe.")
        
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Erro ao verificar/criar o banco de dados: {err}")

class Products(SQLModel,table=True):
    id : Optional[int] = Field(default=None,primary_key=True)
    product_name : str
    reviews : float
    reviews_qtd : int
    product_price_local : str
    product_price : float
    insert_date : str

def create_engine_sqlmodel():
    engine = create_engine(f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')
    SQLModel.metadata.create_all(engine)
    return engine

def inserir_dados_csv(dtframe,engine):
    df = dtframe

    with Session(engine) as session:
        for _, row in df.iterrows():
            produto = Products(
                product_name=row['product_name'],
                reviews=float(row['reviews']),
                reviews_qtd=int(row['reviews_qtd']),
                product_price_local=row['product_price_local'],
                product_price=float(row['product_price']),
                insert_date=row['insert_date']
            )
            session.add(produto)
        session.commit()
        print("Dados inseridos com sucesso!")

if __name__ == '__main__':
    print(verificar_database())
    create_engine_sqlmodel()