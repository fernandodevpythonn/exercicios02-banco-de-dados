def criar_tabela(cursor):
  cursor.execute("""
      CREATE TABLE IF NOT EXISTS cliente (
       idcliente INT AUTO_INCREMENT PRIMARY KEY,
       nome VARCHAR(45) NOT NULL,
       email VARCHAR(100) NOT NULL UNIQUE,
       cartao INT(11) NOT NULL UNIQUE
      )
  """)
  cursor.execute("""
      CREATE TABLE IF NOT EXISTS veiculo(
        idveiculo INT AUTO_INCREMENT PRIMARY KEY,
        modelo VARCHAR(45) NOT NULL,
        marca VARCHAR(45) NOT NULL,
        adicional VARCHAR(100) NOT NULL,
        cor VARCHAR(45) NOT NULL
      )
  """)
  cursor.execute("""
      CREATE TABLE IF NOT EXISTS local(
        idlocal INT AUTO_INCREMENT PRIMARY KEY,
        rua VARCHAR(100) NOT NULL,
        numero INT NOT NULL         
      )
  """)
  cursor.execute("""
      CREATE TABLE IF NOT EXISTS contrato(
       idcontrato INT AUTO_INCREMENT PRIMARY KEY,
       veiculo_idveiculo INT NOT NULL,
       cliente_idcliente INT NOT NULL,
       local_idlocal INT NOT NULL,
       FOREIGN KEY (veiculo_idveiculo) REFERENCES veiculo(idveiculo),      
       FOREIGN KEY (cliente_idcliente) REFERENCES cliente(idcliente),
       FOREIGN KEY (local_idlocal) REFERENCES local(idlocal)
      )
  """)

def cadastrar_cliente(cursor,nome,email,cartao):
  cursor.execute("""
     INSERT INTO cliente (nome,email,cartao)               
     VALUES(%s,%s,%s)
  """, (nome,email,cartao))

def cadastrar_veiculo(cursor,modelo,marca,cor,adicional):
  cursor.execute("""
     INSERT INTO veiculo (modelo,marca,cor,adicional)
     VALUES(%s,%s,%s,%s)
  """, (modelo,marca,cor,adicional))

def cadastrar_local(cursor,rua,numero):
  
  cursor.execute("""
     INSERT INTO local (rua,numero)
     VALUES (%s,%s)
  """, (rua, numero))

def cadastrar_contrato(cursor,cliente_idcliente,veiculo_idveiculo,local_idlocal):
  cursor.execute("""
     INSERT INTO contrato (cliente_idcliente,veiculo_idveiculo,local_idlocal)
     VALUES (%s,%s,%s)
  """, (cliente_idcliente,veiculo_idveiculo,local_idlocal))