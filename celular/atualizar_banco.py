import sqlite3 as sq

def atualizar(nome):
    conexao = sq.connect('imagens.db')
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO img (nome) VALUES(?)''', [nome])
    conexao.commit()
    return True

