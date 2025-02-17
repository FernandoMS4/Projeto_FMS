import requests
import pandas as pd
import re

df = pd.read_json( '../../archive/produtos_250216_193351.jsonl',
                dtype='str',
                lines=True)


# teste = 'https://www.mercadolivre.com.br/controle-joystick-feir-fr-202-preto/p/MLB15146710#polycard_client=search-nordic&searchVariation=MLB15146710&wid=MLB5016108280&position=26&search_layout=grid&type=product&tracking_id=96545ca5-2577-4303-a1b5-365743287cc5&sid=search'
# teste = 'https://produto.mercadolivre.com.br/MLB-3899849881-smartphone-samsung-galaxy-s23-plus-256gb-verde-excelente-_JM#polycard_client=search-nordic&position=34&search_layout=stack&type=item&tracking_id=c6b75b27-0c53-4c2a-9fc1-ef7a7a9bbf28'
# teste = teste.replace('-','')
# print(re.search(r"MLB(\d+)", teste).group(1))

df['product_id'] = df['product_url'].str.replace('-','').apply(lambda url: re.search(r"MLB(\d+)", url).group(1) if re.search(r"MLB(\d+)", url) else '')
df = df[(df['product_id'] != '')]
print(df)