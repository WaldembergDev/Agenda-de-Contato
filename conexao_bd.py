import psycopg2

def fechar_conexoes(cur, con):
    cur.close()
    con.close()
    
def criar_conexao():
    con = psycopg2.connect(host='localhost', database='agenda_contato', user='postgres', password='acnppnj0206', port='5433')
    return con

def visualizar_contatos():
    try:
        con = criar_conexao()
        cur = con.cursor()
        sql = "SELECT * FROM contatos"
        cur.execute(sql)
        resultados = cur.fetchall()
        for index, (id, nome, telefone) in enumerate(resultados):
            print(f'{id:<3} - {nome:^20} - {telefone:^15}')
    except Exception as error:
        print("Erro ao acessar o PostgreSQL:", error)
    finally:
        fechar_conexoes(cur, con)


def adicionar_contato(contato, numero):
    try:
        con = criar_conexao()
        cur = con.cursor()
        sql = f"""INSERT INTO contatos (nome, telefone)
        VALUES (%s,%s)"""
        cur.execute(sql, (contato, numero))
        con.commit()

        print('Contato Adicionado com sucesso!')
    except Exception as error:
        print("Erro ao acessar o PostgreSQL:", error)
    
    finally:
        fechar_conexoes(cur, con)

def editar_contato(id_contato, novo_contato):
    try:
        con = criar_conexao()
        cur = con.cursor()
        sql = """SELECT nome FROM contatos WHERE id_contato = %s"""
        cur.execute(sql, (id_contato,))
        resultados = cur.fetchall()
        if len(resultados) < 1:
            print('Contato não encontrado!')
        else:
            sql = """UPDATE contatos
             SET nome = %s 
             WHERE id_contato = %s"""
            cur.execute(sql, (novo_contato, id_contato))
            con.commit()
            print('Contato modificado com sucesso!')
    except Exception as error:
        print("Erro ao acessar o PostgreSQL:", error)
    
    finally:
        fechar_conexoes(cur, con)

def remover_contato(contato):
    try:
        con = criar_conexao()
        cur = con.cursor()
        sql = """SELECT nome FROM contatos WHERE nome = %s"""
        cur.execute(sql, (contato,))
        resultados = cur.fetchall()
        if len(resultados) < 1:
            print('Contato não encontrado!')
        else:
            sql = """DELETE FROM contatos WHERE nome = %s"""
            cur.execute(sql, (contato,))
            con.commit()
            print('Contato removido com sucesso!')

    except Exception as error:
        print("Erro ao acessar o PostgreSQL:", error)
    
    finally:
        fechar_conexoes(cur, con)
