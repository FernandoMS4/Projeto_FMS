from sqlmodel import (
    Field,
    SQLModel,
    Session,
    create_engine,
    select,
    Column,
    TIMESTAMP,
    text,
)
from sqlalchemy.dialects.mysql import insert
from sqlalchemy import String
from typing import Optional
import mysql.connector
import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime


class Products(SQLModel, table=True):
    """
    Esta tabela serve para armazenar os produtos do scrapping
    """
    product_name: str = Field(default=None, primary_key=True)
    reviews: float
    reviews_qtd: int
    product_price_local: str
    product_price_from: float
    product_price_to: float = Field(default=None, primary_key=True)
    created_date: datetime = Field(
        default=datetime.now().strftime('%y-%m-%d %H:%M:%S')
    )
    modified_date: datetime
    marketplace: str
    product_url: str = Field(sa_type=String(4000))
    product_image: str = Field(sa_type=String(4000))


class Market_Places(SQLModel, table=True):
    id: str = Field(default=None, primary_key=True)
    marketplace_name: str


class Status_User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(sa_type=String(40))
    created_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP,
            server_default=text('CURRENT_TIMESTAMP'),
            nullable=False,
            onupdate=datetime.now,
        )
    )


class Role(SQLModel, table=True):

    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=40, nullable=False)
    create_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False
        )
    )
    update_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP,
            server_default=text('CURRENT_TIMESTAMP'),
            onupdate=datetime.now,
            nullable=False,
        )
    )


class Users(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, nullable=False)
    email: str = Field(default=None, max_length=70, nullable=True)
    password: str = Field(default=None, max_length=40, nullable=True)
    create_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False
        )
    )
    update_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP,
            server_default=text('CURRENT_TIMESTAMP'),
            onupdate=datetime.now,
            nullable=False,
        )
    )
    status_id: int = Field(
        default=1, foreign_key='status_user.id', nullable=False
    )
    email_confirmed: bool = Field(default=None, nullable=True)
    hash_email_confirm: str = Field(default=None, max_length=80, nullable=True)


class StatusUser(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=40)
    create_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False
        )
    )
    update_at: datetime = Field(
        default_factory=datetime.now,
        sa_column_kwargs={'onupdate': datetime.now},
    )


class Roles(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=40)
    create_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False
        )
    )
    update_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP,
            server_default=text('CURRENT_TIMESTAMP'),
            nullable=False,
            onupdate=datetime.now,
        )
    )


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100)
    email: Optional[str] = Field(default=None, max_length=70)
    password: Optional[str] = Field(default=None, max_length=40)
    create_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False
        )
    )
    update_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP,
            server_default=text('CURRENT_TIMESTAMP'),
            nullable=False,
            onupdate=datetime.now,
        )
    )
    status_id: int = Field(foreign_key='status_user.id', default=1)
    email_confirmed: Optional[bool] = Field(default=None)
    hash_email_confirm: Optional[str] = Field(default=None, max_length=20)


class Roles_Users(SQLModel, table=True):
    user_id: int = Field(foreign_key='users.id', primary_key=True)
    role_id: int = Field(foreign_key='roles.id', primary_key=True)


class Tokens(SQLModel, table=True):
    token: str = Field(primary_key=True)
    refresh_token: str
    expiration: datetime
    user_id: int = Field(foreign_key='users.id')


class Hash_Tokens_Password(SQLModel, table=True):
    token: str = Field(primary_key=True)
    expiration: datetime
    user_id: int = Field(foreign_key='users.id')


class Genders(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=40)
    create_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False
        )
    )
    update_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP,
            server_default=text('CURRENT_TIMESTAMP'),
            nullable=False,
            onupdate=datetime.now,
        )
    )


class User_Details(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    birth_date: datetime
    create_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False
        )
    )
    update_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP,
            server_default=text('CURRENT_TIMESTAMP'),
            nullable=False,
            onupdate=datetime.now,
        )
    )
    user_id: int = Field(foreign_key='users.id')
    gender_id: int = Field(foreign_key='genders.id')
    gender_additional_details: Optional[str] = Field(
        default=None, max_length=70
    )


class Addresses(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    number: Optional[str] = Field(default=None, max_length=12)
    street: str = Field(max_length=70)
    neighborhood: Optional[str] = Field(default=None, max_length=50)
    state: Optional[str] = Field(default=None, max_length=40)
    country: Optional[str] = Field(default=None, max_length=70)
    cep: Optional[str] = Field(default=None, max_length=12)
    additional_address_details: Optional[str] = Field(
        default=None, max_length=40
    )
    lat: Optional[float] = Field(default=None)
    lng: Optional[float] = Field(default=None)
    city: Optional[str] = Field(default=None, max_length=100)
    create_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False
        )
    )
    update_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP,
            server_default=text('CURRENT_TIMESTAMP'),
            nullable=False,
            onupdate=datetime.now,
        )
    )


class Addresses_User_Details(SQLModel, table=True):
    user_detail_id: Optional[int] = Field(default=None, primary_key=True)
    address_id: int = Field(foreign_key='addresses.id')


class Email_Templates(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    message: str
    template_identifier: str = Field(max_length=30)
    create_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False
        )
    )
    update_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP,
            server_default=text('CURRENT_TIMESTAMP'),
            nullable=False,
            onupdate=datetime.now,
        )
    )


class Settings(SQLModel, table=True):
    id: int = Field(primary_key=True)
    expiration_token_hours: int = Field(default=2)


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
    """
    Função que verifica se o database existe no ambiente e o cria caso não exista\n
    Variaveis passadas no  arquivo .env conforme necessidade\n
    Connector: MysqlConnector

    """
    try:
        connection = mysql.connector.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD
        )
        cursor = connection.cursor()

        cursor.execute(f"show databases like '{DB_NAME}'")
        result = cursor.fetchone()

        if not result:
            cursor.execute(f'CREATE DATABASE {DB_NAME}')
            print(f"Banco de dados '{DB_NAME}' criado com sucesso.")
        else:
            print(f"Banco de dados '{DB_NAME}' já existe.")

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f'Erro ao verificar/criar o banco de dados: {err}')


def create_engine_sqlmodel():
    engine = create_engine(
        f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    )
    SQLModel.metadata.create_all(engine)
    return engine


def buscar_lista_url(engine):
    with Session(engine) as session:
        markets = select(Market_Places.marketplace_name)
        lista_market = session.exec(markets).all()
        listas = []
        for i in lista_market:
            listas.append(i.lower)
    return listas


def inserir_dados_csv(dtframe, engine):
    df = dtframe

    with Session(engine) as session:
        for i, linha in df.iterrows():
            consulta = (
                insert(Products)
                .values(
                    product_name=linha['product_name'],
                    reviews=float(linha['reviews']),
                    reviews_qtd=int(linha['reviews_qtd']),
                    product_price_local=linha['product_price_local'],
                    product_price_from=linha['product_price_from'],
                    product_price_to=float(linha['product_price_to']),
                    modified_date=linha['modified_date'],
                    marketplace=linha['marketplace'],
                    product_url=linha['product_url'],
                    product_image=linha['product_image'],
                )
                .on_duplicate_key_update(
                    product_name=linha['product_name'],
                    reviews=float(linha['reviews']),
                    reviews_qtd=int(linha['reviews_qtd']),
                    product_price_local=linha['product_price_local'],
                    product_price_from=linha['product_price_from'],
                    product_price_to=float(linha['product_price_to']),
                    modified_date=linha['modified_date'],
                    marketplace=linha['marketplace'],
                    product_url=linha['product_url'],
                    product_image=linha['product_image'],
                )
            )
            session.exec(consulta)
        session.commit()
        print('Dados inseridos com sucesso!')


if __name__ == '__main__':
    print(verificar_database())
    create_engine_sqlmodel()
