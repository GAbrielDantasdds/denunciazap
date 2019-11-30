import socket

def enviar(dado):
    ip = 'endereço de ip da sua máquina'
    port = 7000 
    addr = ((ip,port)) 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client_socket.connect(addr) 
    mensagem = dado
    mensagem = bytes(dado, encoding='utf-8')
    client_socket.send(mensagem)
    print('mensagem enviada') 
    client_socket.close()


