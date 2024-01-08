import mysql.connector
from mysql.connector import errorcode

## acessar pela pasta :   C:\Program Files\MySQL\MySQL Server 8.0\bin

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")
cursor.execute("CREATE DATABASE `jogoteca`;")
cursor.execute("USE `jogoteca`;")

# criando tabelas
# criando tabelas
TABLES = {}
TABLES['Enterprise'] = ('''
        CREATE TABLE IF NOT EXISTS `Enterprise` (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(20) NOT NULL,
        cnpj VARCHAR(14) NOT NULL,
        contact VARCHAR(12) NOT NULL,
        email VARCHAR(50) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Levels'] = ('''
        CREATE TABLE IF NOT EXISTS `Levels` (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        id_enterprise INT,
        name VARCHAR(20) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_enterprise) REFERENCES enterprise(id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['URLs'] = ('''
        CREATE TABLE IF NOT EXISTS `URLs` (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        id_levels INT,
        url VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_levels) REFERENCES levels(id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Products'] = ('''
        CREATE TABLE IF NOT EXISTS `Products` (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        id_enterprise INT, 
        name VARCHAR(50) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_enterprise) REFERENCES enterprise(id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Users'] = ('''
        CREATE TABLE IF NOT EXISTS `Users` (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        id_levels INT,
        name VARCHAR(20) NOT NULL,
        trading_name VARCHAR(20) NOT NULL,
        cnpj VARCHAR(14) NOT NULL,
        contact VARCHAR(12) NOT NULL,
        nickname VARCHAR(15) NOT NULL,
        password VARCHAR(100) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_levels) REFERENCES levels(id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Notifications'] = ('''
        CREATE TABLE IF NOT EXISTS `Notifications` (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        id_users INT,
        message VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_users) REFERENCES users(id),
        FOREIGN KEY (id_products) REFERENCES products(id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Farmer'] = ('''
        CREATE TABLE IF NOT EXISTS `Farmer` (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        id_users INT,
        cotact VARCHAR(12) NOT NULL,
        email VARCHAR(50) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_users) REFERENCES users(id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


TABLES['City'] = ('''   
        CREATE TABLE IF NOT EXISTS `City` (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(20) NOT NULL,
        uf VARCHAR(2) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


TABLES['Farm'] = ('''
        CREATE TABLE IF NOT EXISTS `Farm` (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        id_farmer INT,
        id_city INT,
        name VARCHAR(20) NOT NULL,
        area FLOAT(10) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_farmer) REFERENCES farmer(id),
        FOREIGN KEY (id_city) REFERENCES city(id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Observations'] = ('''
        CREATE TABLE IF NOT EXISTS `Observations` (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        id_farm INT,
        id_users INT,
        message VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_farm) REFERENCES farm(id),
        FOREIGN KEY (id_users) REFERENCES users(id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Visity'] = ('''
        CREATE TABLE IF NOT EXISTS `Visity` (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        id_farm INT,
        id_users INT,
        date DATE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_farm) REFERENCES farm(id),
        FOREIGN KEY (id_users) REFERENCES users(id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Obs_visity'] = ('''
        CREATE TABLE IF NOT EXISTS `Obs_visity` (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        id_visity INT,
        id_users INT,
        message VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_visity) REFERENCES visity(id),
        FOREIGN KEY (id_users) REFERENCES users(id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Media'] = ('''
        CREATE TABLE IF NOT EXISTS `Media` (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        id_farm INT,
        id_users INT,
        type VARCHAR(20) NOT NULL,
        url VARCHAR(255) NOT NULL,
        latitude FLOAT(10) NOT NULL,
        longitude FLOAT(10) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_farm) REFERENCES farm(id),
        FOREIGN KEY (id_users) REFERENCES users(id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela in TABLES:
        tabela_sql = TABLES[tabela]
        try:
                print('Criando tabela {}:'.format(tabela), end=' ')
                cursor.execute(tabela_sql)
        except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                        print('Já existe')
                else:
                        print(err.msg)
        else:
                print('OK')

## inserindo exemplos para simulação
enterprise_sql = 'INSERT INTO enterprise (name, cnpj, contact, email) VALUES (%s, %s, %s, %s)'
# Dados fictícios para inserção nas tabelas
data = {}

data["enterprises"] = [
        ("ABC Company", "12345678901234", "987654321", "abc@example.com"),
        ("XYZ Corporation", "98765432109876", "123456789", "xyz@example.com")
]

data["levels"] = [
        (1, "Interno"),
        (1, "Médio"),
        (1, "Avançado"),
        (2,"Inicial"),
        (2,"Intermediário"),
        (2,"Avançado")
]

data["urls"] = [
        (1, "https://exemplo.com/nivel1"),
        (2, "https://exemplo.com/nivel2"),
        (3, "https://exemplo.com/nivel3")
]

data["products"] = [
        (1, "Ferramenta A"),
        (2, "Software B")
]

data["users"] = [
        (1, "João",  'TradingCo', '12345678901234', '987654321', 'joao123', 'senha123'),
        (2, "Maria", 'TechBiz', '98765432109876', '123456789', 'maria_tech', 'segura123')
]

data["notifications"] = [
        (1, "Primeira notificação para usuário 1"),  # Substitua os IDs 1 e 1 pelos IDs reais dos usuários
        (2, "Segunda notificação para usuário 2"),  # Substitua os IDs 2 e 2 pelos IDs reais dos usuários
]

data["farmer_data"] = [
        (1, '987654321', 'jose@example.com'),  # Substitua o ID 1 pelo ID real do usuário associado
        (2, '999999999', 'ana@example.com'),  # Substitua o ID 2 pelo ID real do usuário associado
        ]


data["cities"] = [
        ("São Paulo", "SP"),
        ("Rio de Janeiro", "RJ")
]

data["farm"] = [
        (1, 1, 'Sítio do José', 100.5),  #
        (2, 2, 'Chácara da Ana', 75.2),  # Substitua o ID 2 pelo ID real do agricultor e da cidade associados
        ]


data["observations"] = [
        (1, 1,"Muito bonito!"),
        (2, 2, "Legal!")
]

data["visits"] = [
        (1, 1, '2023-01-15'),
        (2, 2, '2023-02-20')
]

data["obs_visits"] = [
        (1, 1, "Fazenda muito bonita!"),
        (2, 2, "Conheci os campos!")
]

data["media"] = [
        (1, 1,'Foto', 'https://exemplo.com/foto1', -23.5505, -46.6333),
        (2, 2,'Vídeo', 'https://exemplo.com/video1', -22.9068, -43.1729)
]



# Loop para inserir dados em cada tabela
for table_name, table_data in data.items():
        columns = ', '.join(table_data['columns'])
        placeholders = ', '.join(['%s'] * len(table_data['columns']))
        insert_query = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'

        cursor.executemany(insert_query, table_data['values'])
        print(f'Dados inseridos na tabela {table_name}')

# Exemplo de exibição dos resultados de uma tabela para confirmar as inserções (opcional)
cursor.execute('SELECT * FROM Enterprise')
print(' -------------  Empresas:  -------------')
for row in cursor.fetchall():
        print(row)  # Aqui você pode ajustar o print para exibir as colunas desejadas

conn.commit()

cursor.close()
conn.close()


