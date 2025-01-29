from src.etl.etl_scrap import format_scrapy_amazon, format_scrapy_mercado_livre
from src.etl.data_base_config import (
    verificar_database,
    create_engine_sqlmodel,
    inserir_dados_csv,
    buscar_lista_url,
)
from src.coleta_mercado.captura_mercado import captura_produtos_mercado_livre
import shutil
from datetime import datetime
import json
import os

if __name__ == '__main__':

    if os.path.exists('data') == False:
        os.mkdir('data')
    if os.path.exists('archive') == False:
        os.mkdir('archive')

    url = [
        'https://lista.mercadolivre.com.br/samsung-galaxy-s23-ultra-(esim)-5g-256-gb-verde-12-gb'
    ]

    reprocess: bool = False
    if reprocess == False:
        for i in url:
            with open('data/produtos.jsonl', 'a', encoding='utf-8') as file:
                for i in captura_produtos_mercado_livre(url=i):
                    file.write(json.dumps(i, ensure_ascii=False) + '\n')

    df = format_scrapy_mercado_livre(reprocess=reprocess)
    #verificar_database()
    engines = create_engine_sqlmodel()
    inserir_dados_csv(df, engine=engines)
    data_hora = datetime.now().strftime('%y%m%d_%H%M%S')
    try:
        try:
            shutil.move(
                'data/produtos.jsonl', f'archive/produtos_{data_hora}.jsonl'
            )
        except:
            print('Arquivo de dados json não encontrado'),
    except KeyError as e:
        print(e)
