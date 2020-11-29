import socket

ip='127.0.0.1'
porta=8000

def client():
    listaComandi = ['F', 'B', 'R', 'L']
    listaPotenze = [int(n) for n in range(0, 10)]
    print(listaComandi)
    print(listaPotenze)

    print("creo istanza")
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate

    c.connect((ip,porta))
    print("connect")

    print("Enter 'exit' to end the connection")
    msg = input("->")  # take input

    while True:
        try:
            c.sendall(msg.encode())  # send message
        except:
            print(f"failed")

        data = c.recv(4096).decode()  # receive response
        print(f"Received from server: {data}")  # show response
        data = (data.split(","))[1]
        lista_istruzioni = []
        for d in data:
            comando = []
            if d in listaComandi:
                comando.append(d)
                data = data.removeprefix(d)
                potenza = ""
                for num in data:
                    if int(num) in listaPotenze:
                        potenza += num
                        data = data.removeprefix(num)
                comando.append(potenza)
            lista_istruzioni.append(tuple(comando))
        print(lista_istruzioni)
        msg = input("->")  # again take input

        if msg == "exit":
            c.sendall(msg.encode())  # send message
            print("Close the connection")
            break

    c.close()  # close the connection


if __name__ == '__main__':
    client()