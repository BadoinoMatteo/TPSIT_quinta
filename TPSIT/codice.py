#Badoino matteo 23/02/2021

"""
//import
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app=Flask(__name__)
"""

"""
//gestione db
db_connection = sqlite3.connect('db.db')
db_cursor = db_connection.cursor()
psw=db_cursor.execute('SELECT ..... FROM ......')
"""

"""
//flask
@app.route('/index/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
    return render_template('accesso.html')
    return render_template('index.html')
"""

"""
//client
import socket

ip='127.0.0.1'
porta=6000

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip,porta))
data=(client.recv(4096).decode())
    risultato=str(eval(data))
client.sendall(risultato.encode())

//server

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #crezione server multiThreading
   s.bind((ip,porta))
   contClient=1
   s.listen()
   conn, addr= s.accept()
    print(f"client collegato: {addr}")
    cl=clientThread(addr[0], addr[1], conn, contClient) #chiamata alla classe
    cl.start()
"""


"""
//chiamata main
if __name__ == '__main__':
    app.run(debug=True)
    """

"""
//client per inoltro messaggio http
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ipServer, porta))
    body = "username=matteo&password=1234"
    msg = f"POST http://127.0.0.1:5000/index/ HTTP/1.1\r\n" \
          f"Host:  http://127.0.0.1:5000\r\n" \
          f"Content-Length: {len(body)}\r\n" \
          f"Content-Type: application/x-www-form-urlencoded\r\n" \
          f"\r\n"\
          f"{body}"
    print(msg)
    client.sendall(msg.encode())
    data = (client.recv(4096)).decode()
    print(data)
"""