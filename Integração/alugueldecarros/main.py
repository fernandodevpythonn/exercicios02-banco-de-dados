from banco_de_dados import iniciar_sistema,conectar
from banco_de_dados.tabela import *

iniciar_sistema()

def menu():
  print("1 - cadastrar cliente")
  print("2 - cadastrar veiculo")
  print("3 - cadastrar local")
  print("4 - cadastrar contrato")

def main():
  while True:
   menu()
   opcao = input("escolha uma opção: ")

   conexao = conectar()
   cursor = conexao.cursor()
   
   match opcao:
    case "1":
        cadastrar_cliente(cursor,
                        input("nome:"),
                        input("email: "),
                        int(input("cartao: ")))
        conexao.commit()
        print("cliente cadastrado")
    case "2":
       cadastrar_veiculo(cursor,
                         input("modelo: "),
                         input("marca: "),
                         input("cor: "),
                         input("adicionais: "))
       conexao.commit()
       print("veiculo cadastrado")
    case "3":
       cadastrar_local(cursor,
                       input("Rua: "),
                       int(input("Número: ")))
       conexao.commit()
       print("local cadastrado")
    case "4":
       cadastrar_contrato(cursor,
                          int(input("id cliente: ")),
                          int(input("id veiculo: ")),
                          int(input("id local: ")))
       conexao.commit()
       print("contrato cadastrado")
main()