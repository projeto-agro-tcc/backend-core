# Projeto Monitoramento Para Agro

Este repositório é destinado ao desenvolvimento do backend de um projeto voltado para a área de monitoramento agrícola, nele será possível administrar e tomar algumas decisões através da análise de algumas variáveis disponíveis no sistema.
Todo desenvolvido utiliando o framework django_restframework.

[![Github Badge](https://img.shields.io/badge/-Github-000?style=flat-square&logo=Github&logoColor=white&link=https://github.com/osvaldosneto)](https://github.com/projeto-agro-tcc/osvaldo-backend)

## Tecnologias
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> V 3.0.0 or upper <br>
<img src="https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white"/> V 8.0 <br>
<img src="https://img.shields.io/badge/InfluxDB-22ADF6?style=for-the-badge&logo=InfluxDB&logoColor=white"/> <br>
<img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray"/> <br>



## Setup

Primeiramente clone o repositório

```sh
$ git clone https://github.com/projeto-agro-tcc/osvaldo-backend.git
$ cd sample-django-app
```

Crie e ative um ambiente virtual

```sh
$ virtualenv venv
$ source venv/bin/activate
```

Instale as dependências

```sh
(env)$ pip install -r requirements.txt
```

Uma vez que as dependências estejam instaladas rode o comando.

```sh
(env)$ cd osvaldo-backend
(env)$ python manage.py runserver
```

Finalmente navegue até o endereço 'http://127.0.0.1:8000'
