DEBUG = True
SQLALCHEMY_DATABASE_URI = \
    '{SGDB}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGDB = 'mysql+mysqlconnector',     #não só o sistema de banco mas também o conector
        usuario = 'root',
        senha = 'admin',
        servidor = '127.0.0.1',      #ou localhost
        database = 'uniao_flask'
        ) #string de conexão com o banco de dados ==== [string modelo: SGDB://usuario:senha@servidor/database]