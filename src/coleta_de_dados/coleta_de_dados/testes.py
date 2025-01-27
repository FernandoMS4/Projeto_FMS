import json
from dotenv import load_dotenv, find_dotenv
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime

def captura_produtos_mercado_livre():
    url_01 = 'https://lista.mercadolivre.com.br/controle-sem-fio#D[A:Controle%20sem%20fio]'
    response = requests.get(url_01)
    if response.status_code == 200:
        soup = bs(response.text, "html.parser")
        produtos = soup.find_all('div',class_='andes-card poly-card poly-card--grid-card andes-card--flat andes-card--padding-0 andes-card--animated')
        print(len(produtos))
        #print(produtos[0].find('img',class_='poly-component__picture')['src'])
        for produto in produtos:

            product_name = produto.find('a',class_='poly-component__title').get_text(strip=True)
            reviews = produto.find('span', class_= 'poly-reviews__rating')
            reviews_qtd = produto.find('span',class_='poly-reviews__total')
            product_price_local = produto.find('span',class_='andes-money-amount__currency-symbol').get_text(strip=True)
            product_price_from = produto.find('s',class_='andes-money-amount andes-money-amount--previous andes-money-amount--cents-comma')    
            product_price_from_cents = '0'
            if product_price_from is not None:
                product_price_from_cents = product_price_from.find('span',class_='andes-money-amount__cents')
                if product_price_from_cents is not None:
                    product_price_from_cents = product_price_from.find('span',class_='andes-money-amount__cents').text
            product_price_to = produto.find('div', class_='poly-price__current').find('span',class_='andes-money-amount__fraction').text
            product_price_to_cents = produto.find('div', class_='poly-price__current').find('span',class_='andes-money-amount__cents')
            product_url = produto.find('a')['href']
            product_img = produto.find('img',class_='poly-component__picture')['src']

            yield {'product_name' : product_name,
                'reviews': '0' if reviews is None else reviews.get_text(strip=True),
                'reviews_qtd' : '0' if reviews_qtd is None else reviews_qtd.get_text(strip=True),
                'product_price_local' : product_price_local,
                'product_price_from_fraction' : '0' if product_price_from is None else product_price_from.find('span',class_='andes-money-amount__fraction').get_text(strip=True),
                'product_price_from_cents' : '0' if product_price_from_cents is None else product_price_from_cents,
                'product_price_to': product_price_to,
                'product_price_to_cents' : '0' if  product_price_to_cents is None else product_price_to_cents.text,
                'product_url' : product_url,
                'product_image' : product_img,
                'modified_date' : datetime.now().strftime("%y%m%d_%H%M%S")
                   }

if __name__ == '__main__':
    with open('../../../data/produtos.jsonl',"a",encoding='utf-8') as file:   
        for i in captura_produtos_mercado_livre():
            file.write(json.dumps(i, ensure_ascii=False) +"\n")
    #captura_produtos_mercado_livre()