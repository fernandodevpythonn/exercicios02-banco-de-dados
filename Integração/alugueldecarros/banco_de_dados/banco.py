import mysql.connector
from mysql.connector import Error

def criar_banco():
  conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
  )
  cursor = conexao.cursor()

  cursor.execute("""
    SELECT SCHEMA_NAME 
        FROM information_schema.SCHEMATA 
        WHERE SCHEMA_NAME = 'alugueldecarros'
  """)

  existe = cursor.fetchone()

  if not existe:
    cursor.execute(
       "CREATE DATABASE alugueldecarros DEFAULT CHARACTER SET utf8"
    )
    print("banco de dados criado com sucesso")
  else:
    print("banco de dados já existe")
  
  conexao.close()
  cursor.close()
def conectar():
  try:
    return mysql.connector.connect(
      host = "localhost",
      user = "root",
      password = "",
      database = "alugueldecarros"
    )
  except Error as e:
    print("erro ao conectar ao banco ",e)
    return None