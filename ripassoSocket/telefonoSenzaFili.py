import socket

#server
def main():
    ipPros="192.168.0.119"
    portaPros=7000
    mioip="192.168.0.117"
    mioPorta=7000
    while True:
        server=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind((mioip, mioPorta))
        data, addres= server.recvfrom(4096)
        print(data.decode())
        server.close()
        #client
        client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.sendto(data, (ipPros,portaPros))
        print("mandato")
        client.close()


if __name__ == '__main__':
    main()