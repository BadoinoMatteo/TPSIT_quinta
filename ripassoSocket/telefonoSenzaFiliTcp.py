import socket

def main():
    ipPros = "192.168.0.123"
    portaPros = 7000
    mioip = "192.168.0.117"
    mioPorta = 7000
    #server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        server.bind((mioip, mioPorta))
        server.listen()
        conn, address= server.accept()
        data=conn.recv(4096)
        print(data.decode())
        server.close()
        #client
        client.connect((ipPros, portaPros))

        client.sendall(data)
        print("mandato")
        client.close()

if __name__ == '__main__':
    main()