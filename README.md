# praticing*django*

Estuding django

- migrando para banco PostgreSQL
`comandos`
`acessar shell postgres (windows)`
- psql -U postgres
`lista todos os bancos`
- \l
`criar banco`
- CREATE DATABASE (nome do banco);
`sair`
- \q
`drive para django e postgres`
- pip install psycopg2
`para usar variaveis de ambient`
- pip install python-dotenv

## Django_Master

ˋcomandos djangoˋ

- criado projeto
  python django-admin startproject core .
- rodar projeto
  python manage.py runserver
- criando app
  python manage.py startapp + nome
- criar as tabelas no banco
  python manage.py migrate
- fazendo mudancas e criar os arquivos de migracoes
  python manage.py makemigrations
- criando super usuario admin
  python manage.py createsuperuser user>admin

### Django Shell

`python manage.py shell`  

#### ACESSO-SGBD

- USER DE TESTE EM NUVEM => admin
- EMAIL PARA TESTE EM NUVEM =>admin@teste.com
- PASS DE TESTE EM NUVEM => Admin$50001
- NOVO USUARIO PARA TESTAR: teste_user
- PASS : Teste@123
- NOVO USUARIO PARA TESTAR: user_teste2
- PASS : Teste2*300

- instalar pacote
  pip install + nome do pacote
- fazer os testes
  python manage.py test

  `Fluxo do Django Framework`

  ![Fluxo-Django](https://github.com/davipythonweb/praticing_django_/blob/main/django-architecture.webp?raw=true)


- implementar docker com mysql com Django