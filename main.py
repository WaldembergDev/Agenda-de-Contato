from conexao_bd import *
import psycopg2

def main():
    print('''Bem vindo ao sistema de contatos.
          Selecione uma opção abaixo:
          1 - Visualizar contatos
          2 - Incluir contato
          3 - Editar contato
          4 - Remover contato
          5 - Limpar todos os contatos
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
        id_contato = int(input('Digite o id do contato que deseja alterar: '))
        resultado = encontrar_contato(id_contato)
        print(resultado)
        if resultado:
            tipo_alteracao = int(input('Digite 1 p/ nome, 2 p/ numero: '))
            if tipo_alteracao == 1:
                novo_nome = input('Digite o novo nome do contato: ')
                editar_nome_contato(id_contato, novo_nome)
            elif tipo_alteracao == 2:
                novo_numero = input('Digite o numero do contato: ')
                editar_numero_contato(id_contato, novo_numero)
            else:
                print('Valor inválido! Retornando ao menu...')

    elif opcao == 4:
        contato = input('Digite o id do contato: ')
        remover_contato(contato)

    elif opcao == 5:
        confirmacao = int(input('Confirma a exclusão de todos os contatos: \n1 p/ sim e 0 p/ não'))
        if confirmacao:
            remover_todos_contatos()
        else:
            print('Retornando ao menu...')

    elif opcao == 0:
        opcao = False
        print('Saindo do programa!')

    else:
        print('Opção inválida!')
    
        