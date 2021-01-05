import socket
import threading
import sqlite3


ip='192.168.1.19'
porta=7000
def main():
    listathread=[]
    nomeFile="percorsi.db"
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip,porta))
    print("metto in ascolto il server")
    s.listen()
    while True:
        conn, addr = s.accept()
        cl=clientThread(conn, addr, nomeFile)
        cl.start()
        listathread.append(cl)


class clientThread(threading.Thread):

    def __init__(self, connection, address, DB_nome):
        threading.Thread.__init__(self)
        self.Server_connection = connection
        self.Server_address = address
        self.DB_nome = DB_nome
        ip = ""
        for i in self.Server_address[0].split("."): ip += str(i)
        ip += "_" + str(self.Server_address[1])
        #self.log = Log(f"{4096}log_{ip}.txt")


    def run(self):

        #self.log.i('thread started, start data transmission with server')

        while True:
            # connessione al database
            db_connection = sqlite3.connect(self.DB_nome)
            db_cursor = db_connection.cursor()

            # carico lista località per controllo
            lista_localita = []
            for row in db_cursor.execute('SELECT luoghi.nome FROM luoghi'): lista_localita.append(row[0])

            # ricezione dati dal client
            data = self.Server_connection.recv(4096).decode()  # receive data
            print(data)

            #self.log.i(f"from connected user {self.Server_address}:  {data}")

            # controllo se finire connessione
            if not data or data == "exit":
                # if data is not received or data is the word 'exit' to end the connection break
                #self.log.i(f"Close connection user {self.Server_address}")
                self.Server_connection.close()  # close the connection
                break

            # split dato in arrivo - end,start
            localita = data.split(",")
            print(localita)
            print(lista_localita)

            # controllo se le due località esistono
            if localita[0] in lista_localita and localita[1] in lista_localita:
                print(f"from connected user {self.Server_address}:  valid data")
                #self.log.i(f"from connected user {self.Server_address}:  valid data")
            else:
                # se una delle due non esiste dico al client di reinserire end,start
                #self.log.e(f"1.2, from connected user {self.Server_address} start or end not found re-enter end,start")
                self.Server_connection.send(f"1.2,start or end not found re-enter end,start".encode())
                # chiusura database
                db_connection.close()
                continue

            # provo a cercare il percorso tra start e end
            try:
                print(f"SELECT percorsi.percorso FROM percorsi WHERE percorsi.id = (SELECT inizio_fine.id_percorso "
                      f"FROM inizio_fine WHERE inizio_fine.id_end = (SELECT luoghi.id FROM luoghi "
                      f"WHERE luoghi.nome = {localita[0]}) AND inizio_fine.id_start = "
                      f"(SELECT luoghi.id FROM luoghi WHERE luoghi.nome = {localita[1]}));")
                percorso = []
                print("eseguo query")
                for row in db_cursor.execute(f'SELECT percorsi.percorso FROM percorsi WHERE percorsi.id = '
                                             f'(SELECT inizio_fine.id_percorso FROM inizio_fine WHERE '
                                             f'inizio_fine.id_end = '
                                             f'(SELECT luoghi.id FROM luoghi WHERE luoghi.nome = "{localita[0]}") '
                                             f'AND inizio_fine.id_start = (SELECT luoghi.id FROM luoghi '
                                             f'WHERE luoghi.nome = "{localita[1]}"));'):
                    percorso = row
                print("query eseguita")
                percorso = str(percorso[0]).upper()
                #self.log.i(f"Risultato query: {percorso}")
            except:
                print("non va")
                # se il percorso tra start e end non esiste dico al client di reinserire end,start
                #self.log.e(f"1.1, from connected user {self.Server_address} path not found re-enter end,start")
                self.Server_connection.send(f"1.1,path not found re-enter end,start".encode())
                # chiusura database
                db_connection.close()
                continue

            # chiusura database
            db_connection.close()
            #self.log.i(f"For the connected user {self.Server_address}:  0.0,{percorso}")
            # invio al client il percorso
            self.Server_connection.send(f"0.0,{percorso}".encode())  # send data to the client

        self.Server_connection.close()


if __name__ == '__main__':
    main()