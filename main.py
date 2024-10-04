from conexao_bd import *
import psycopg2

def main():
    print('''Bem vindo ao sistema de contatos.
          Selecione uma opção abaixo:
          1 - Visualizar contatos
          2 - Incluir contato
          3 - Editar contato
          4 - Remover contato
          0 - Sair do sistema''')

opcao = True

while opcao:
    main()
    opcao = int(input('Selecione a opção desejada: '))
    if opcao == 1:
        visualizar_contatos()
    elif opcao == 2:
        contato = input('Digite o nome do contato: ')
        numero = input('Digite o numero do contato:')
        adicionar_contato(contato, numero)
    elif opcao == 3:
        contato_antigo = input('Digite o nome do contato antigo: ')
        contato_novo = input('Digite o novo nome para o contato escolhido: ')
        editar_contato(contato_antigo, contato_novo)
    elif opcao == 4:
        contato = input('Digite o nome do contato: ')
        remover_contato(contato)
    elif opcao == 0:
        opcao = False
        print('Saindo do programa!')
    else:
        print('Opção inválida!')
    
        