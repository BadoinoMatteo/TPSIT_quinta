import re
import socket
import time
import requests
import AlphaBot

# 0.0,B50R90F600L90F400
# B 50  R 90    F 600   L 90    F 400
# [(b, 50), ]s

ipServer='192.168.43.90'
porta=7000

def client():
    print("creo istanza")
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
    print("cerco server")
    c.connect((ipServer,porta))
    print("connect")

    address = c.getsockname()
    ip = ""
    for i in address[0].split("."): ip += str(i)
    ip += "_" + str(address[1])
    #log = Log("client.txt")
    #log.i("Creazione Server")
    #log.i("connect")

    print("Enter 'exit' to end the connection")
    mex = input() # take input
    print(mex)
    alphabot=AlphaBot
    print("ok")
    while True:
        try:
            print(c)
            c.sendall(mex.encode())  # send message
            print("mandato")
        except:
            print("failed")

        data = c.recv(4096).decode()  # receive response
        print("Received from server " + data)  # show response
        data = (data.split(","))[1]
        lista_potenze = re.split('B|R|F|L', data)
        lista_potenze.pop(0)
        regex = ''
        for index, el in enumerate(lista_potenze):
            if index == len(lista_potenze) - 1:
                regex += el
            else:
                regex += el + '|'
        lista_direzioni = re.split(regex, data)
        lista_direzioni.pop(-1)
        comandi = []
        for index, el in enumerate(lista_potenze): comandi.append((lista_direzioni[index], int(el)))
        print(comandi)
        print(el)
        for el in comandi:
            istruction(alphabot, el[0])
            time.sleep(1)
        msg = input("->")  # again take input

        if msg == "exit":
            c.sendall(msg.encode())  # send message
            print("Close the connection")
            break

    c.close()  # close the connection


def istruction(alphabot, command):
    switcher = {
        "F": alphabot.forward,
        "B": alphabot.backward,
        "R": alphabot.right,
        "L": alphabot.left
    }
    switcher[command]()


if __name__ == '__main__':
    client()