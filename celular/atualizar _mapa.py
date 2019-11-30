from servidor import receber
from marcarMapa import marcarLoc

while True:
    local = receber()
    with open('locations.csv', 'a') as arquivo:
        arquivo.write(f'{local}')
    arquivo.close()
    marcarLoc()
    
