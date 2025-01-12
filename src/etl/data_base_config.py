from sqlmodel import  Field,SQLModel,Session,create_engine,select
from sqlalchemy.dialects.mysql import insert
import mysql.connector
import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime

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
    product_name : str = Field(default=None,primary_key=True)
    reviews : float
    reviews_qtd : int
    product_price_local : str
    product_price : float = Field(default=None,primary_key=True)
    created_date : str = Field(default=datetime.now().strftime("%y/%m/%d %H:%M:%S"))
    modified_date : str
    marketplace : str

class Market_Places(SQLModel,table=True):
    id:str = Field(default=None,primary_key=True)
    marketplace_name : str

def create_engine_sqlmodel():
    engine = create_engine(f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')
    SQLModel.metadata.create_all(engine)
    return engine

def buscar_lista_url(engine):
    with Session(engine) as session:
        markets = select(Market_Places.marketplace_name)
        lista_market = session.exec(markets).all()
        listas = []
        for i in lista_market:
            listas.append(i)
    return listas

def inserir_dados_csv(dtframe,engine):
    df = dtframe

    with Session(engine) as session:
        for i, linha in df.iterrows():
            consulta = insert(Products).values(
                product_name = linha['product_name'],
                reviews = float(linha['reviews']),
                reviews_qtd = int(linha['reviews_qtd']),
                product_price_local = linha['product_price_local'],
                product_price =float(linha['product_price']),
                modified_date = linha['modified_date'],
                marketplace = linha['marketplace']
            ).on_duplicate_key_update(
                product_name = linha['product_name'],
                reviews = float(linha['reviews']),
                reviews_qtd = int(linha['reviews_qtd']),
                product_price_local = linha['product_price_local'],
                product_price =float(linha['product_price']),
                modified_date = linha['modified_date'],
                marketplace = linha['marketplace']
            )
            session.exec(consulta)
        session.commit()
        print("Dados inseridos com sucesso!")

if __name__ == '__main__':
    print(verificar_database())
    create_engine_sqlmodel()