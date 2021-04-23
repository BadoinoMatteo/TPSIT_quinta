import time
import requests
def main():
    while True:
        print("1-> grandezze\n 2->stazioni\n 3->inserimento\n 4->valori")
        scelta=input("inserisci numero operazione da eseguire")
        menu(scelta)

def IdGrandezza():  #funzione che chiama la web api per l'id della grandezza
    nome=input("inserisci nome grandezza")
    URL = "http://127.0.0.1:5000/grandezze" #url web api
    PARAMS={'nome': nome}   #paramentri necessari
    r= requests.get(url=URL, params=PARAMS) #chiamata web api
    print(r.text)

def idStazione(): #funzione che chiama la web api per l'id della stazione
    nome=input("inserisci nome stazione")
    URL = "http://127.0.0.1:5000/stazioni"  #url web api
    PARAMS={'stazioni': nome}   #paramentri necessari
    r= requests.get(url=URL, params=PARAMS) #chiamata web api
    print(r.text)

def inserimento(): #funzione che chiama la web api per l'inserimento della misurazione
    idGrandezza=input("inserisci id grandezza")
    idStazione = input("inserisci id stazione")
    valore=input("inserisci valore")
    URL = "http://127.0.0.1:5000/inserimentoMisurazione" #url web api
    PARAMS={'valore': valore, 'idGrandezza':idGrandezza, 'idStazione':idStazione} #parametri necessari
    r=requests.get(url=URL, params=PARAMS)  #chiamata web api
    print(r.text)

def valori(): #funzione che chiama la web api per ottenere i valori minimi, massimi, medi
    idGrandezza = input("inserisci id grandezza")
    idStazione = input("inserisci id stazione")
    URL = "http://127.0.0.1:5000/valoriMediMinimiMassimi"   #url web api
    PARAMS = {'idGrandezza': idGrandezza, 'idStazione': idStazione}     #parametri necessari
    r=requests.get(url=URL, params=PARAMS)  #chiamata
    print(r.text)


def menu(scelta):
    switcher = {
        "1": IdGrandezza,
        "2": idStazione,
        "3": inserimento,
        "4": valori
    }
    switcher[scelta]()

if __name__ == '__main__':
    main()