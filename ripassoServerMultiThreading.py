import  socket
import  threading

ip='192.168.88.88'
porta=8000

def main():
   s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.bind((ip,porta))
   listathread=[]
   s.listen()
   while True:
    conn, addr= s.accept()
    clientThread(addr[0], addr[1], conn)
    listathread.append(conn)


class clientThread(threading.Thread):
    def __init__(self, ip, p, conn):
        threading.Thread.__init__(self)
        self.ip_address= ip
        self.porta=p
        self.connessione=conn
        def run(self):
            while True:
                clientThread.start()
                data = clientThread.recv(4096)
                print(data.decode())
                clientThread.sendall(data)
            for i in clientThread:
                clientThread[i].join()



if __name__ == '__main__':
    main()