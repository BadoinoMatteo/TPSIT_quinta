import re
import requests
import time
import datetime
import threading

from AlphaBot import AlphaBot

alphabot = AlphaBot

def main():
    path = threading.Thread(target=percorso)
    sensor = threading.Thread(target=sensore)

def sensore():
    URL = "http://192.168.43.90:5000/api/v1/resources/db"
    precDR=0
    precDS=0
    while True:
        inDR = alphabot.sensoreDestro
        inDL = alphabot.sensoreSinistro
        if inDR != precDR:
            #cambiamento sensore di destra
            print("cambio sensore destra")
            precDR=inDR
            data=str(datetime.date.today())
            PARAMS = {'lato': "DR", 'date': data}
            print("mando")
            requests.get(url=URL, params=PARAMS)
            print("mandato")
        if inDL!=precDS:
            # cambio sensore di sinistra
            print("cambio sensore di sinistra")
            precDS=inDL
            data=str(datetime.date.today())
            PARAMS = {'lato': "DL", 'date': data}
            requests.get(url=URL, params=PARAMS)




"""def percorso():
    url="http://127.0.0.1:5000/api/v1/resources/path"
    print("ciao")
    PARAMS={'start': "aula3.0",
            'end': "info1"}
    print("ok")
    r=requests.get(url=url, params=PARAMS)
    data=r.json()
    print(data)
    comandi = split_istruzioni(data[0]['percorso'])
    print(comandi)
    for el in comandi:
        print(f"{el[0]} di {el[1]}")
    #istruction(alphabot, el[0])
    #time.sleep(el[1])
    #alphabot.stop()


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
    for index, el in enumerate(lista_potenze): comandi.append((lista_direzioni[index], int(el)))
    return comandi


def istruction(alphabot, command):
    switcher = {
        "F": alphabot.forward,
        "B": alphabot.backward,
        "R": alphabot.right,
        "L": alphabot.left
    }
    switcher[command]()
"""

if __name__ == '__main__':
    #main()
    sensore()