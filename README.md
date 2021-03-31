# Weather Api
Projeto com o propósito de aprendizado na linguagem Python, o microframework Flask e a lib ORM SQLAlchemy.

### Tecnologias utilizadas: 
* Python, versão 3.9.2
* Docker
* PostgreSQL
* Flask
* SQLAlchemy
* Git

### Ferramentas utilizadas:
* Visual Studio Code
* Postman
* DBeaver
* PIP

### Dependências do Projeto
Todas as dependências estão listadas no requirements.txt, porém há o destaque na lib PyOWM, utilizada no projeto. Ela funciona como um wrapper das API's da plataforma OpenWeatherMap. A sua documentação pode ser consultada [aqui](https://pyowm.readthedocs.io/en/latest/index.html#).

A collection do Postman pode ser baixada por [aqui](https://app.blackhole.run/#MVyBd58CbO1LaaMFDDuKJVczUHF5E2mkXVrcPPJPWFw7).

### Estrutura
O arquivo config.py é responsável pela importação e configuração da conexão com o banco de dados. O client.py, possui o propósito também de configuração, porém do objeto da lib PyOWM, a qual será utilizado no restante do projeto. No arquivo models.py, possui o mapeamento da tabela Histórico, cujo servirá para visualizar as consultas realizadas anteriormente na API. O arquivo app.py é o arquivo principal, onde fica mapeado os endpoint's e alguns métodos auxiliares para realizar de/para de objeto para dicionário, por exemplo. 


## Demonstração

![alt text](https://github.com/joseph-alexandre/weather-api/blob/main/Apresentação%20Weather%20Api.gif)

## Instalação e execução do projeto

Necessário possuir instalado:
* Python versão 3.x.x
* Docker

Na raiz do projeto, utilizar o seguinte comando para criar um ambiente virtual no Python:
> python -m venv [path/to/myenv]

A seguir, ative-o:
> ./path/to/myenv/Scripts/activate

Ainda na raiz do projeto e com o ambiente virtual ativado, utilize o comando a seguir para instalar as dependências:
> pip install -r requirements.txt

Criar um arquivo .env dentro da raíz do projeto, informando a key da API do OpenWeatherMap, no formato a seguir:
> API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXX"

Agora, suba o PostgreSQL:
> docker-compose up database

E então, execute a aplicação:
> cd flaskr  
> python -m flask run

## O que falta?

* Testes automatizados.
* Containerizar a própria API. Atualmente, só o banco de dados está containerizado.
* Implementar opções de filtro para a consulta de histórico.
* Implementar mais tratamentos e validações em casos de erros.
* Implementar outros endpointers de consulta, adicionando parâmetros para uma consulta mais precisa; atualmente é utilizado apenas o nome da cidade.
* Documentação da API, descrição aprofundada do que cada endpoint retorna e seus parâmetros.
* Tratamento de TimeZone e formatação de pontos flutuantes em alguns campos.
* Implementar a consulta de previsão dos próximos cinco dias.

