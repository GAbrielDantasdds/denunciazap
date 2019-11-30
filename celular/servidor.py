import socket
def receber():
    host = '' 
    port = 7000 
    addr = (host, port) 
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    serv_socket.bind(addr) 
    serv_socket.listen(10)  
    con, cliente = serv_socket.accept() 
    mapa = con.recv(1024)
    mapa = bytes.decode(mapa)
    print(mapa)
    serv_socket.close()
    return mapa

