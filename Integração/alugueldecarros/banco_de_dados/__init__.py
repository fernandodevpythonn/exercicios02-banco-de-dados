from .banco import criar_banco,conectar
from .tabela import criar_tabela

def iniciar_sistema():
  criar_banco()
  conexao = conectar()
  if conexao is not None:
    cursor = conexao.cursor()
    criar_tabela(cursor)
    conexao.commit()
    cursor.close()
    conexao.close()
iniciar_sistema()