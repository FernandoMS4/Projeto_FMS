import pandas as pd

def format_scrapy():
    try:
        df = pd.read_json('D:\PROJETO_WEBSCRAP_FMS\data\data_amazon_final.jsonl',lines=True)
    except KeyError as e :
        return print(f"Não foi possível ler o arquivo: {e}")
    df['reviews'] = df['reviews'].str.split(' ').str[0].fillna('0.0').str.replace(',','.').astype('float')
    df['reviews_qtd'] = df['reviews_qtd'].fillna('0').astype('int')
    df['product_price_local'] = df['product_price_local'].fillna('R$')
    df['product_price'] = df['product_price'].fillna('0').astype('int')
    df['product_price'] = df['product_price'].astype('str') + '.' + df['product_price_fraction'].fillna('0').astype('int').astype('str')
    df['product_price'] = df['product_price'].astype('float')
    df['marketplace'] = 'amazon'
    df = df.drop(columns='product_price_fraction')
    df = df.drop_duplicates()
    df.to_csv('data/dados_tratados.csv',header=True,index=False)
    return df

if __name__ == '__main__':
    df = format_scrapy()
    df.to_csv('data/dados_tratados.csv',header=True,index=False)