from src.etl.etl_scrap import format_scrapy
from src.etl.data_base_config import verificar_database,create_engine_sqlmodel,inserir_dados_csv

if __name__ == '__main__':
    df = format_scrapy()
    verificar_database()
    engines = create_engine_sqlmodel()
    inserir_dados_csv(df,engine=engines)