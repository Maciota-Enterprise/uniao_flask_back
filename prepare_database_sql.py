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

cursor.execute("DROP DATABASE IF EXISTS `uniao_flask`;")
cursor.execute("CREATE DATABASE `uniao_flask`;")
cursor.execute("USE `uniao_flask`;")

# criando tabelas
TABLES = {}
TABLES['Enterprise'] = ('''
        CREATE TABLE IF NOT EXISTS `Enterprise` (
        `id` INT(11) NOT NULL AUTO_INCREMENT,
        `name` VARCHAR(20) NOT NULL,
        `cnpj` VARCHAR(14) NOT NULL,
        `contact` VARCHAR(12) NOT NULL,
        `email` VARCHAR(50) NOT NULL,
        `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        `last_modified` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Levels'] = ('''
        CREATE TABLE IF NOT EXISTS `Levels` (
        id INT NOT NULL AUTO_INCREMENT,
        id_enterprise INT,
        name VARCHAR(20) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_enterprise) REFERENCES Enterprise(id),
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['URLs'] = ('''
        CREATE TABLE IF NOT EXISTS `URLs` (
        id INT NOT NULL AUTO_INCREMENT,
        id_levels INT,
        url VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_levels) REFERENCES Levels(id),
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Products'] = ('''
        CREATE TABLE IF NOT EXISTS `Products` (
        id INT NOT NULL AUTO_INCREMENT,
        id_enterprise INT, 
        name VARCHAR(50) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_enterprise) REFERENCES Enterprise(id),
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Users'] = ('''
        CREATE TABLE IF NOT EXISTS `Users` (
        id INT NOT NULL AUTO_INCREMENT ,
        id_levels INT,
        name VARCHAR(20) NOT NULL,
        trading_name VARCHAR(20) NOT NULL,
        contact VARCHAR(12) NOT NULL,
        email VARCHAR(50) NOT NULL,
        password VARCHAR(200) NOT NULL,
        active TINYINT(1) NOT NULL DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_levels) REFERENCES Levels(id),
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Business_group'] = ('''
        CREATE TABLE IF NOT EXISTS `Business_group` (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(20) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Notifications'] = ('''
        CREATE TABLE IF NOT EXISTS `Notifications` (
        id INT NOT NULL AUTO_INCREMENT ,
        id_users INT,
        message VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_users) REFERENCES Users(id),
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Client'] = ('''
        CREATE TABLE IF NOT EXISTS `Client` (
        id INT NOT NULL AUTO_INCREMENT ,
        id_users INT,
        id_group INT,
        empresarial_name VARCHAR(20) NOT NULL,
        fantasy_name VARCHAR(20) NOT NULL,
        cnpj VARCHAR(14) NOT NULL,
        bairro VARCHAR(20) NOT NULL,
        cep VARCHAR(8) NOT NULL,
        address VARCHAR(50) NOT NULL,
        number INT NOT NULL,
        city VARCHAR(20) NOT NULL,
        uf VARCHAR(2) NOT NULL,
        email VARCHAR(50) NOT NULL,
        b2b TINYINT(1) NOT NULL DEFAULT 0,
        venda_direta TINYINT(1) NOT NULL DEFAULT 0,
        revenda TINYINT(1) NOT NULL DEFAULT 0,
        active TINYINT(1) NOT NULL DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_users) REFERENCES Users(id),
        FOREIGN KEY (id_group) REFERENCES Business_group(id),
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['City'] = ('''   
        CREATE TABLE IF NOT EXISTS `City` (
        id INT NOT NULL AUTO_INCREMENT ,
        name VARCHAR(20) NOT NULL,
        uf VARCHAR(2) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')


TABLES['Farm'] = ('''
        CREATE TABLE IF NOT EXISTS `Farm` (
        id INT NOT NULL AUTO_INCREMENT ,
        id_client INT,
        id_city INT,
        name VARCHAR(20) NOT NULL,
        area FLOAT(10) NOT NULL,
        contact VARCHAR(12) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_client) REFERENCES Client(id),
        FOREIGN KEY (id_city) REFERENCES City(id),
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Observations'] = ('''
        CREATE TABLE IF NOT EXISTS `Observations` (
        id INT NOT NULL AUTO_INCREMENT ,
        id_farm INT,
        id_users INT,
        message VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_farm) REFERENCES farm(id),
        FOREIGN KEY (id_users) REFERENCES Users(id),
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Visity'] = ('''
        CREATE TABLE IF NOT EXISTS `Visity` (
        id INT NOT NULL AUTO_INCREMENT ,
        id_farm INT,
        id_users INT,
        date DATE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_farm) REFERENCES farm(id),
        FOREIGN KEY (id_users) REFERENCES Users(id),
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Obs_visity'] = ('''
        CREATE TABLE IF NOT EXISTS `Obs_visity` (
        id INT NOT NULL AUTO_INCREMENT ,
        id_visity INT,
        id_users INT,
        message VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_visity) REFERENCES visity(id),
        FOREIGN KEY (id_users) REFERENCES Users(id),
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES["Documents"] = ('''
        CREATE TABLE IF NOT EXISTS `Documents` (
        id INT NOT NULL AUTO_INCREMENT ,
        id_client INT,
        url VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_client) REFERENCES Client(id),
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Media'] = ('''
        CREATE TABLE IF NOT EXISTS `Media` (
        id INT NOT NULL AUTO_INCREMENT ,
        id_farm INT,
        id_users INT,
        type VARCHAR(20) NOT NULL,
        url VARCHAR(255) NOT NULL,
        latitude FLOAT(10) NOT NULL,
        longitude FLOAT(10) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (id_farm) REFERENCES Farm(id),
        FOREIGN KEY (id_users) REFERENCES Users(id),
        PRIMARY KEY (`id`)
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

data["Enterprise"] = {
        "columns": ["name", "cnpj", "contact", "email"],
        "values": [
                ("ABC Company", "12345678901234", "987654321", "abc@example.com"),
                ("XYZ Corporation", "98765432109876", "123456789", "xyz@example.com")
        ]
}

data["Levels"] = {
        "columns": ["id_enterprise", "name"],
        "values": [
                (1, "Interno"),
                (1, "Médio"),
                (1, "Avançado"),
                (2, "Inicial"),
                (2, "Intermediário"),
                (2, "Avançado")
        ]
}

data["URLs"] = {
        "columns": ["id_levels", "url"],
        "values": [
                (1, "https://exemplo.com/nivel1"),
                (2, "https://exemplo.com/nivel2"),
                (3, "https://exemplo.com/nivel3")
        ]
}

data["Products"] = {
        "columns": ["id_enterprise", "name"],
        "values": [
                (1, "Ferramenta A"),
                (2, "Software B")
        ]
}

data["Users"] = {
        "columns": ["id_levels", "name", "trading_name", "contact", "email", "password"],
        "values": [
                (1, "João",  'TradingCo',  '987654321', 'joao123@hotmail.com', 'senha123'),
                (2, "Maria", 'TechBiz', '123456789', 'maria_tech@hotmail.com', 'segura123')
        ]
}

data["Business_group"] = {
        "columns": ["id","name"],
        "values": [
                (1,"Grupo A"),
                (2,"Grupo B"),
                (3,"Grupo C")
        ]
}

data["Notifications"] = {
        "columns": ["id_users", "message"],
        "values": [
                (1, "Primeira notificação para usuário 1"),  
                (2, "Segunda notificação para usuário 2"),  
        ]
}

data["client"] = {
        "columns": ["id_users", "id_group", "email", "empresarial_name", "fantasy_name", "cnpj", "bairro", "cep", "address", "number", "city", "uf", "b2b", "venda_direta", "revenda", "active"],
        "values": [
        (1, 1, 'jose@example.com',  'Empresarial Name 1', 'Fantasy Name 1','12345678901234', 'Bairro 1', '12345678', 'Adress 1', '123', 'City 1', 'UF',False, False, True, True),
        (2, 2, 'andre@example.com',  'Empresarial Name 2', 'Fantasy Name 2','12345678901234', 'Bairro 2', '12345678', 'Adress 2', '123', 'City 2', 'UF',False, False, True, True), 
        ]
}


data["City"] = {
        "columns": ["name", "uf"],
        "values": [
        ("Jaboticabal", "SP"),  
        ("Ribeirão Preto", "SP"),  
        ]
}

data["Farm"] = {
        "columns": ["id_client", "id_city", "name", "area", "contact"],
        "values": [
        (1, 1, 'Sítio do José', 100.5, '987654321'),  
        (2, 2, 'Chácara da Ana', 75.2, '123456789'),  
        ]
}

data["Observations"] = {
        "columns": ["id_farm", "id_users", "message"],
        "values": [
        (1, 1,"Muito bonito!"),
        (2, 2, "Legal!")
        ]
}

data["Visity"] = {
        "columns": ["id_farm", "id_users", "date"],
        "values": [
        (1, 1, '2023-01-15'),
        (2, 2, '2023-02-20')
        ]
}

data["Obs_visity"] = {
        "columns": ["id_visity", "id_users", "message"],
        "values": [
        (1, 1, "Fazenda muito bonita!"),
        (2, 2, "Conheci os campos!")
        ]
}

data["Media"] = {
        "columns": ["id_farm", "id_users", "type", "url", "latitude", "longitude"],
        "values": [
        (1, 1,'Foto', 'https://exemplo.com/foto1', -23.5505, -46.6333),
        (2, 2,'Vídeo', 'https://exemplo.com/video1', -22.9068, -43.1729)
        ]
}

# loop para inserir dados em cada tabela
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
        print(row)

cursor.execute('SELECT * FROM Levels')
for row in cursor.fetchall():
        print(row)

cursor.execute('SELECT * FROM URLs')
for row in cursor.fetchall():
        print(row)

conn.commit()

cursor.close()
conn.close()


