import sqlite3 as sq

def verificar(nome):
    conexao = sq.connect('imagens.db')
    cursor = conexao.cursor()
    cursor.execute('''SELECT nome FROM img;''')
    nomes = cursor.fetchall()
    nome = [nome]
    for ele in nomes:
        if nome == list(ele): print('sim')
        return True
    return False

