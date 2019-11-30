import glob
def atualizar():
    log = glob.glob('*jpeg')
    with open('log.txt', 'r+') as arquivo:
        for elemento in log:
            for j in arquivo:
                if f'{elemento}\n' == f'{j}':
                    pass
                else:
                    arquivo.write(f'{elemento}\n')
        arquivo.close()

