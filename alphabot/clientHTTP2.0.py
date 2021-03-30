import re
import requests
import time
import datetime
import threading

from AlphaBot import AlphaBot

alphabot = AlphaBot()
alphabot.stop()

def main():
    path = threading.Thread(target=percorso())
    sensor = threading.Thread(target=sensore())
    sensor.start()
    path.start()
    path.join()
    sensor.join()

def sensore():
    URL = "http://192.168.43.90:5000/api/v1/resources/db"
    stato = "fermo"
    print(stato)
    while True:
        print(stato)
        Dr = alphabot.sensoreDestro()
        Dl = alphabot.sensoreSinistro()
        print(f"DR_status: {Dr} - DL_status: {Dl}")
        if Dl == 1 and Dr == 1 and stato != "libero":
            # tutto libero
            stato = "libero"
        if Dl == 0 and Dr == 0 and stato != "ostacolo":
            # ostacolo davanti
            stato = "ostacolo"
        if Dl == 1 and Dr == 0 and stato != "sx_libero":
            # ostacolo davanti
            stato = "sinistra_libero"
        if Dl == 0 and Dr == 1 and stato != "destra_libero":
            # ostacolo davanti
            stato = "destra_libero"
        time.sleep(1)




def percorso():
    url="http://192.168.43.90:5000/api/v1/resources/path"
    #print("ciao")
    PARAMS={'start': "aula3.0",
            'end': "info1"}
    #print("ok")
    r=requests.get(url=url, params=PARAMS)
    data=r.json()
    #print(data)
    comandi = split_istruzioni(data[0]['percorso'])
    #print(comandi)
    for el in comandi:
        continue
        #print(f"{el[0]} di {el[1]}")
    istruction(alphabot, el[0])
    time.sleep(el[1])
    alphabot.stop()


def split_istruzioni(percorso):
    alphabot.stop()
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
        istruction(alphabot,comandi)
        alphabot.stop()


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
    #sensore()