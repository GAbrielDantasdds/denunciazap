import sqlite3 as sq

def criar():
    conexao = sq.connect('imagens.db')
    cursor = conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS img (nome TEXT);''')
    print('tabela criada')

criar()
