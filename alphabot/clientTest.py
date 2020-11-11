import socket

def main():
    client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = "127.0.0.1"
    porta = 8000
    message = ""

    client.connect((ip, porta))

    while True:
        message = input("inserisci messaggio da mandare")

        client.sendall(message.encode())

    s.close()

if __name__ == '__main__':
    main()