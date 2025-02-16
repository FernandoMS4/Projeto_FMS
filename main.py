from src.etl.etl_scrap import format_scrapy_mercado_livre
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

    verificar_database()
    engines = create_engine_sqlmodel()

    url = [
        'https://lista.mercadolivre.com.br/controle-sem-fio#D[A:controle%20sem%20fio]',
        'https://lista.mercadolivre.com.br/bíblia-da-mulher-de-fé%2C-nvi%2C-couro-soft%2C-lírios-do-campo%2C-de-walsh%2C-sheila.-editorial-vida-melhor-editora-s.a-em-portugu#D[A:Bíblia%20da%20Mulher%20de%20Fé,%20NVI,%20Couro%20Soft,%20Lírios%20do%20Campo,%20de%20Walsh,%20Sheila.%20Editorial%20Vida%20Melhor%20Editora%20S.A%20em%20portugu]',
        'https://lista.mercadolivre.com.br/livro-bíblia-da-mulher-de-fé%2C-nvi%2C-letra-grande%2C-couro-soft#D[A:Livro%20Bíblia%20Da%20Mulher%20De%20Fé,%20Nvi,%20Letra%20Grande,%20Couro-soft]',
        'https://lista.mercadolivre.com.br/samsung-galaxy-s23-ultra-(esim)-5g-256-gb-verde-12-gb',
        'https://lista.mercadolivre.com.br/escova-secadora-modeladora-revlon-root-booster-rvdr5292#D[A:Escova%20Secadora%20Modeladora%20Revlon%20Root%20Booster%20Rvdr5292]',
        'https://lista.mercadolivre.com.br/climatizador-de-ar-wap-air-protect-135w-painel-touch-led-cor-branco-127v#D[A:Climatizador%20De%20Ar%20Wap%20Air%20Protect%20135w%20Painel%20Touch%20Led%20Cor%20Branco%20127V]',
        'https://lista.mercadolivre.com.br/fritadeira-elétrica-wap-air-fryer-barbecue-12-em-1-1800w-127v#D[A:Fritadeira%20Elétrica%20Wap%20Air%20Fryer%20Barbecue%2012%20em%201%201800W%20127V]',
        'https://lista.mercadolivre.com.br/escada-de-alumínio#D[A:Escada%20de%20Alumínio]'
        ,'https://lista.mercadolivre.com.br/fone-de-ouvido#D[A:fone%20de%20ouvido]'
        ,'https://lista.mercadolivre.com.br/cueca_Noindex_True'
        ,'https://lista.mercadolivre.com.br/cabo-usb_Noindex_True'
        ,'https://lista.mercadolivre.com.br/carregador_Noindex_True'
        ,'https://lista.mercadolivre.com.br/tenis_Noindex_True'
    ]

    reprocess: bool = False
    if reprocess == False:
        for i in url:
            with open('data/produtos.jsonl', 'a', encoding='utf-8') as file:
                for i in captura_produtos_mercado_livre(url=i):
                    file.write(json.dumps(i, ensure_ascii=False) + '\n')

    df = format_scrapy_mercado_livre(reprocess=reprocess)

    engines = create_engine_sqlmodel()

    inserir_dados_csv(df, engine=engines)

    try:
        try:
            data_hora = datetime.now().strftime('%y%m%d_%H%M%S')
            shutil.move(
                'data/produtos.jsonl', f'archive/produtos_{data_hora}.jsonl'
            )
        except:
            print('Arquivo de dados json não encontrado'),
    except KeyError as e:
        print(e)
