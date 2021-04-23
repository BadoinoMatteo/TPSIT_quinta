import socket as sck
import ast
import re
import time

#from AlphaBot import AlphaBot

#alphabot = AlphaBot()
def main():
    c = sck.socket(sck.AF_INET, sck.SOCK_STREAM)  # instantiate
    c.connect(('127.0.0.1', 5000))
    msg = f"GET http://127.0.0.1:5000/api/v1/resources/path?end=info3&&start=aula3.0 HTTP/1.1\r\n" \
          f"Host: http://127.0.0.1:5000/api/v1/resources/path?end=info3&&start=aula3.0\r\n" \
          f"Content-Length: 0\r\n" \
          f"Content-Type: application/x-www-form-urlencoded\r\n" \
          f"\r\n" \
          f" "

    c.sendall(msg.encode())
    data = " "
    percorso = None
    while data != "":
        if "percorso" in data:
            percorso = ast.literal_eval(data)
            break
        data = (c.recv(8192)).decode()
    c.close()
    comandi = split_istruzioni(percorso[0]['percorso'])
    print(comandi)
    for el in comandi:
        print(f"{el[0]} di {el[1]}")
    istruction(alphabot, el[0])
    time.sleep(el[1])
    alphabot.stop()


def split_istruzioni(percorso):
    lista_potenze = re.split('B|R|F|L', percorso)
    # print(lista_potenze)
    lista_potenze.pop(0)
    regex = ''
    for index, el in enumerate(lista_potenze):
        if index == len(lista_potenze) - 1:
            regex += el
        else:
            regex += el + '|'
    lista_direzioni = re.split(regex, percorso)
    lista_direzioni.pop(-1)
    comandi = []
    for index, el in enumerate(lista_potenze):
        comandi.append((lista_direzioni[index], int(el)))
    return comandi


def istruction(alphabot, command):
    switcher = {
        "F": alphabot.forward,
        "B": alphabot.backward,
        "R": alphabot.right,
        "L": alphabot.left
    }
    switcher[command]()


if __name__ == '__main__':
    main()