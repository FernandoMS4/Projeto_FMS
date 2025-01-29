# Projeto_FMS

```
Opa! Bão? 

Este projeto tem como premissa realizar o Web Scrap de produtos do mercado livre com base em listas que os próprios usuários do app me fornecer
estressando o código para ver o desempenho, e como se comporta conforme o volume for aumentando no código
```

#  O projeto

O projeto se iniciou com base no scrapy na Amazon, porém eu queria fazer minhas customizações e ter mais controle do meu código com base em minhas necessidades, então acabei partindo para o requests e beautifulsoup4 e customizei o processo que ficou mais confortávl para mim.

## OBS

Este projeto utiliza o Poetry como gerenciador do meu ambiente virtual.

O banco de dados utilizei o mysql local que pode ser seguido a estrutura a seguir

O projeto ainda não possui middleware, tenho ciência que se eu tentar muitas vezes posso ser bloqueado pelo mercado livre

```
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_PORT = 3306
DB_NAME = "web_scraping"
```

```
TODO: 
    - Implementar logs
    - Implementar Docker
    - Implementar Airflow(ainda vou ver a viabilidade)
    - Verificar possíveis vulnerabilidades
    - Implementar middleware
    - Documentar as funções
```