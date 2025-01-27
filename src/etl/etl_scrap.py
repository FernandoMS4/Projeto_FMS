import pandas as pd


def format_scrapy_amazon():
    try:
        df = pd.read_json(
            'D:\PROJETO_WEBSCRAP_FMS\data\data_amazon_final.jsonl', lines=True
        )
    except KeyError as e:
        return print(f'Não foi possível ler o arquivo: {e}')
    df['reviews'] = (
        df['reviews']
        .str.split(' ')
        .str[0]
        .fillna('0.0')
        .str.replace(',', '.')
        .astype('float')
    )
    df['reviews_qtd'] = df['reviews_qtd'].fillna('0').astype('int')
    df['product_price_local'] = df['product_price_local'].fillna('R$')
    df['product_price'] = df['product_price'].fillna('0').astype('int')
    df['product_price'] = (
        df['product_price'].astype('str')
        + '.'
        + df['product_price_fraction'].fillna('0').astype('str')
    )
    df['product_price'] = df['product_price'].astype('float')
    df['marketplace'] = 'amazon'
    df = df.drop(columns='product_price_fraction')
    df = df.drop_duplicates()
    df.to_csv('data/dados_tratados.csv', header=True, index=False)
    return df

def format_scrapy_mercado_livre():
    """
    Lê o arquivo coletado json e realiza o tratamento dos dados e padroniza de acordo com a tabela de produtos

    """

    try:
        df = pd.read_json(
            'D:\PROJETO_WEBSCRAP_FMS\data\produtos.jsonl',
            lines=True
            )
    except KeyError as e:
        return print(f'Não foi possível ler o arquivo: {e}')
    
    df = df.drop_duplicates()
    df['reviews'] = df['reviews'].astype('float',2)
    df['reviews_qtd'] = df['reviews_qtd'].str.replace('(',' ').str.replace(')',' ').astype('int')
    df['product_price_from'] = (df['product_price_from_fraction'].astype('str').str.replace('.','') + '.' + df['product_price_from_cents'].astype('str')).astype('float')
    df['product_price_to'] = (df['product_price_to'].astype('str').str.replace('.','') + '.' + df['product_price_to_cents'].astype('str')).astype('float')
    df['marketplace'] = 'mercado livre'
    df = df.drop(columns=['product_price_from_fraction','product_price_from_cents','product_price_to_cents'])
    return df

if __name__ == '__main__':
    #df = format_scrapy_amazon()
    #df.to_csv('data/dados_tratados.csv', header=True, index=False)
    format_scrapy_mercado_livre()