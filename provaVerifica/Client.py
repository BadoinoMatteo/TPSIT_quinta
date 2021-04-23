import time
import requests

def main():
    URL_in = "http://127.0.0.1:5000/server/inizializzazione"
    PARAMSstart = {'msg': 'start'}
    start = requests.get(url=URL_in, params=PARAMSstart)
    while True:
        URL_op = "http://127.0.0.1:5000/server/operazione"
        PARAMSrichiesta = {'msg': 'richiesta'}
        operazione = eval(requests.get(url=URL_op, params=PARAMSrichiesta).json())
        #operazione = eval(richiesta.json())
        PARAMSOperazione = {'msg': 'soluzione', 'risultato': operazione}
        requests.get(url=URL_op, params=PARAMSOperazione)
        time.sleep(1)

if __name__ == '__main__':
    main()