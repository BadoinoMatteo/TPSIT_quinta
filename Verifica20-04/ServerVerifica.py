import sqlite3
import flask
from flask import jsonify, request, render_template, session
import datetime

app = flask.Flask(__name__)


@app.route('/grandezze', methods=['GET'])
def grandezze():
    if 'nome' in request.args:                          #controllo prensenza messaggio nell'url
        nomeGrandezza = request.args['nome']
    idGrandezze = letturaGrandezzeId(nomeGrandezza)     #richiamo funzione per lettura su db che restituisce l'id della grandezza in base al nome
    print(idGrandezze)
    return jsonify(idGrandezze)

@app.route('/stazioni', methods=['GET'])
def stazioni():
    if 'stazioni' in request.args:                      #controllo presenza messaggio nell'url
        nomeStazione = request.args['stazioni']
    idStazione = letturaStazioniId(nomeStazione)        #chiamata a funzione per lettura db che restituisce l'id della stazione in base al nome
    print(idStazione)
    return jsonify(idStazione)

@app.route('/inserimentoMisurazione', methods=['GET'])
def inserimentoMisurazione():
    if 'valore' in request.args and 'idGrandezza' in request.args \
    and 'idStazione' in request.args:                      #controllo presenza messaggi richiesti nell'url
        valore = request.args['valore']
        idGrandezza=request.args['idGrandezza']
        idStazione=request.args['idStazione']
        dataOra=datetime.datetime()
    inserimentoMisurazione(valore,idGrandezza,idStazione,dataOra)                   #chiamata funzione per esecuzione query
    return jsonify("inserito")

@app.route('/valoriMediMinimiMassimi', methods=['GET'])
def valoriMediMinimiMassimi():
    if 'idGrandezza' in request.args and 'idStazione' in request.args:                      #controllo presenza messaggi richiesti nell'url
        idGrandezza=request.args['idGrandezza']
        idStazione=request.args['idStazione']
    risultati=valoriDB(idStazione, idGrandezza)
    return jsonify(risultati)


# funzioni per connessione con db
def letturaGrandezzeId(nomeGrandezza):
    db_connection = sqlite3.connect('meteo_db.db')          #connessione al db
    db_cursor = db_connection.cursor()
    for row in db_cursor.execute(f'SELECT id_misura FROM grandezze '                #esecuzione query
                                 f'WHERE grandezza_misurata=="{nomeGrandezza}"'):
        idGrandezze = (row[0])                              #salvataggio risultato query
    db_cursor.close()
    print(idGrandezze)
    return idGrandezze

def letturaStazioniId(nomeStazione):
    db_connection = sqlite3.connect('meteo_db.db')                  #connessione al db
    db_cursor = db_connection.cursor()
    for row in db_cursor.execute(f'SELECT id_stazione FROM stazioni '       #eseguzione query
                                 f'WHERE nome=="{nomeStazione}"'):
        idStazione = (row[0])                           #salvataggio  risultato query
    db_cursor.close()
    print(idStazione)
    return idStazione

def inserimentoMisurazione(valore, idGrandezza, idStazione, dataOra):
    db_connection = sqlite3.connect('meteo_db.db')  # connessione al db
    db_cursor = db_connection.cursor()
    db_cursor.execute(f"INSERT INTO misurazioni ('id_stazione', 'id_grandezza', "         #esecuzione query per inserimento misurazione
                          f"'data_ora', 'valore') "
                          f"VALUES ('{int(idGrandezza)}','{int(idStazione)}', "
                          f"'{dataOra}','{float(valore)}')")
    db_cursor.execute(f"COMMIT;")
    db_cursor.close()

def valoriDB(idStazione, idGrandezza):
    risultati=[]
    db_connection = sqlite3.connect('meteo_db.db')  # connessione al db
    db_cursor = db_connection.cursor()
    for row in db_cursor.execute(f'SELECT avg(valore), max(valore), min(valore) FROM misurazioni '                  #esecuzione query
                                     f'WHERE id_stazione = "{idStazione}" AND id_grandezza = "{idGrandezza}"'):
        risultati.append({'valoreMedio': row[0], 'valoreMassimo':row[1], 'valoreMinimo': row[2]})                   #salvataggio risultati
    db_cursor.close()
    return risultati        #return risultati

if __name__ == '__main__':
    # letturaGrandezzeId("temperatura")
    app.run(host='127.0.0.1', debug='on')
    # grandezze()
