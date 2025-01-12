from src.etl.etl_scrap import format_scrapy
from src.etl.data_base_config import verificar_database,create_engine_sqlmodel,inserir_dados_csv,buscar_lista_url
import shutil
from datetime import datetime

if __name__ == '__main__':
    #df = format_scrapy()
    #verificar_database()
    engines = create_engine_sqlmodel()
    #inserir_dados_csv(df,engine=engines)

    #data_hora = datetime.now().strftime("%y_%m_%d-%H_%M_%S")

    #try:
    #    try:
    #        shutil.move('data/dados_tratados.csv',f'archive/dados_tratados_{data_hora}.csv')
    #    except:
    #        print('Arquivo de dados tratados não encontrado') 
    #    try:   
    #        shutil.move('data/data_amazon_final.jsonl',f'archive/data_amazon_final_{data_hora}.jsonl')
    #    except:
    #         print('Arquivo de dados json não encontrado'),
    #except KeyError as e:
    #    print(e)
    print(buscar_lista_url(engines))