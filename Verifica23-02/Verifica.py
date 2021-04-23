#Badoino matteo 23-02-2021

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import semaforo
import datetime

s=semaforo.semaforo()
STATO='ATTIVO' #semaforo acceso    SPENTO-->semaforo spento
app=Flask(__name__)
TEMPOROSSO=3
TEMPOGIALLO=2
TEMPOVERDE=5

@app.route('/index/', methods=[ 'GET', 'POST'])
def index():
    global STATO, TEMPOROSSO, TEMPOVERDE, TEMPOGIALLO
    #controllo semaforo
    if request.method == 'POST':
        print("ciao")
        comando = str(request.form['comando'])
        print(comando)
        if(comando=="accensione"):
            STATO='ATTIVO'
            controlloDBON()
        else:
            STATO='SPENTO'
            controlloDBOFF()

        if STATO == "ATTIVO":
            s.rosso(TEMPOROSSO)
            s.verde(TEMPOGIALLO)
            s.giallo(TEMPOVERDE)

        if STATO == "SPENTO":
            for _ in range(3):
                s.giallo(TEMPOGIALLO)
                s.luci_spente(1)
    #gestione tempo luci
    if request.method == 'POST':
        modificaRosso = int(request.form['modificaRosso'])
        TEMPOROSSO=modificaRosso
        print(TEMPOROSSO)
        modificaGiallo = int(request.form['modificaGiallo'])
        TEMPOGIALLO = modificaGiallo
        print(TEMPOGIALLO)
        modificaVerde = int(request.form['modificaVerde'])
        TEMPOVERDE = modificaVerde
        print(TEMPOVERDE)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')

def controlloDBON():                #scrittura su db accensione semaforo
    data = f"{datetime.datetime.now()}"
    db_connection = sqlite3.connect('dbVerifica.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute(f"INSERT INTO Controllo('data', 'operazione') VALUES ('data', 'accensione')")
    db_cursor.close()

def controlloDBOFF():                #scrittura su db spegimento semaforo
    data = f"{datetime.datetime.now()}"
    db_connection = sqlite3.connect('dbVerifica.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute(f"INSERT INTO Controllo('data', 'operazione') VALUES ('data', 'spegnimento')")
    db_cursor.close()

