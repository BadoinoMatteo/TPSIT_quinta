#server multithreading

import socket
import threading
import sqlite3

ip='127.0.0.1'
porta=6000


def main():
   s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #crezione server multiThreading
   s.bind((ip,porta))
   contClient=1
   listathread=[]
   listaAddress=[]
   s.listen()
   while True:
    conn, addr= s.accept()
    print(f"client collegato: {addr}")
    cl=clientThread(addr[0], addr[1], conn, contClient) #chiamata alla classe
    cl.start()
    listathread.append(conn)
    listaAddress.append(addr)
    contClient+=1

def leggiDb():
    listaIdclient=[]
    listaOperation=[]
    connDb=sqlite3.connect('operations.db')
    cursorDb=connDb.cursor()
    #mi salvo id client  e operation
    for r in cursorDb.execute('SELECT client, operation FROM operations'):
        listaIdclient.append(r[0])
        listaOperation.append(r[1])
    connDb.close()
    #print(listaIdclient, listaOperation)
    return listaIdclient,listaOperation


class clientThread(threading.Thread):
    def __init__(self, ip, p, conn,cont):
        threading.Thread.__init__(self)
        self.ip_address= ip
        self.porta=p
        self.connessione=conn
        self.id=cont
        print("ciao")
    def run(self):
        while True:
            clientDb, operationDb = leggiDb()
            for i in clientDb:
                if(self.id==i):
                    index=clientDb.index(self.id)
                    operation=operationDb[index]
                    print(operationDb[index])
                    self.connessione.sendall(operation.encode())  # comunicazione con il client
                    print("mandato")
                    risultato=self.connessione.recv(4096).decode() #ricevo dal client il risultato
                    print(f"{operation} = {risultato} from {self.ip_address} - {self.porta}")


        for i in clientThread:
            clientThread[i].join()

if __name__ == '__main__':
    main()