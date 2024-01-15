#instale o mysql-connector-python ao invez do mysql-connector
#caso já tenha instalado o mysql-connector-python, desinstale-o e instale o mysql-connector com o comando: pip install mysql-connector

DEBUG = True
SQLALCHEMY_DATABASE_URI = \
    '{SGDB}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGDB = 'mysql+mysqlconnector',     #não só o sistema de banco mas também o conector
        usuario = 'root',
        senha = 'admin',
        servidor = '127.0.0.1',      #ou localhost
        database = 'uniao_flask'
        ) #string de conexão com o banco de dados ==== [string modelo: SGDB://usuario:senha@servidor/database]