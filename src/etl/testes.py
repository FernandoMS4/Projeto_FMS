import requests

url = 'https://lista.mercadolivre.com.br/fritadeira-elétrica-wap-air-fryer-barbecue-12-em-1-1800w-127v#D[A:Fritadeira%20Elétrica%20Wap%20Air%20Fryer%20Barbecue%2012%20em%201%201800W%20127V]'
response = requests.get(url)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    with open('response_teste.txt', mode='w', encoding='utf-8') as f:
        f.write(response.json)  # Usar response.text para conteúdo HTML ou texto
else:
    print(f"Falha ao obter a página. Código de status: {response.status_code}")
