from src.etl.etl_scrap import format_scrapy_amazon,format_scrapy_mercado_livre
from src.etl.data_base_config import verificar_database,create_engine_sqlmodel,inserir_dados_csv,buscar_lista_url
from src.coleta_mercado.captura_mercado import captura_produtos_mercado_livre
import shutil
from datetime import datetime
import json

if __name__ == '__main__':

    url = ['https://lista.mercadolivre.com.br/controle-sem-fio#D[A:controle%20sem%20fio]',
    'https://lista.mercadolivre.com.br/bíblia-da-mulher-de-fé%2C-nvi%2C-couro-soft%2C-lírios-do-campo%2C-de-walsh%2C-sheila.-editorial-vida-melhor-editora-s.a-em-portugu#D[A:Bíblia%20da%20Mulher%20de%20Fé,%20NVI,%20Couro%20Soft,%20Lírios%20do%20Campo,%20de%20Walsh,%20Sheila.%20Editorial%20Vida%20Melhor%20Editora%20S.A%20em%20portugu]',
    'https://lista.mercadolivre.com.br/livro-bíblia-da-mulher-de-fé%2C-nvi%2C-letra-grande%2C-couro-soft#D[A:Livro%20Bíblia%20Da%20Mulher%20De%20Fé,%20Nvi,%20Letra%20Grande,%20Couro-soft]'
    ]
    for i in url:
        with open('data/produtos.jsonl', 'a', encoding='utf-8') as file:
            for i in captura_produtos_mercado_livre(url=i):
                file.write(json.dumps(i, ensure_ascii=False) + '\n')

    df = format_scrapy_mercado_livre()
    verificar_database()
    engines = create_engine_sqlmodel()
    inserir_dados_csv(df,engine=engines)

    data_hora = datetime.now().strftime("%y%m%d_%H%M%S")

    try:
       try:
           shutil.move('data/dados_tratados.csv',f'archive/dados_tratados_{data_hora}.csv')
       except:
           print('Arquivo de dados tratados não encontrado') 
       try:   
           shutil.move('data/produtos.jsonl',f'archive/produtos_{data_hora}.jsonl')
       except:
            print('Arquivo de dados json não encontrado'),
    except KeyError as e:
       print(e)