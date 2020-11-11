import socket
import threading
import sqlite3

def main():
    ip='127.0.0.1'
    porta=8000
    listathread=[]
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip,porta))
    s.listen()
    while True:
        conn, addr = s.accept()
        clientThread(addr[0], addr[1], conn)
        listathread.append(conn)


class clientThread(threading.Thread):
    def __init__(self, ip, p, conn):
        threading.Thread.__init__(self)
        self.ip_address = ip
        self.porta = p
        self.connessione = conn

        def run(self):
            while True:
                clientThread.start()
                data = clientThread.recv(4096)
                print(data)
                connDb=sqlite3.connect('percorsi.db')
                c=connDb.cursor()
                c.execute(data)
            for i in clientThread:
                clientThread[i].join()


if __name__ == '__main__':
    main()