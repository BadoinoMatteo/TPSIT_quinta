import sqlite3
import flask
from flask import jsonify, request, render_template, session

app = flask.Flask(__name__)

db_connection = sqlite3.connect('db.db')
db_cursor = db_connection.cursor()
lista_client_id = [row[0] for row in db_cursor.execute(f'SELECT DISTINCT idClient FROM Operazioni ')]
db_cursor.close()

app.secret_key="verifica"


@app.route('/server/inizializzazione', methods=['GET'])
def inizializzazione():
    if 'msg' in request.args:
        msg = request.request.args['msg']
        if msg == 'start':
            session['client_id'] = lista_client_id.pop()
            session['lista_operazioni'] = letturaDBOperazione(session['client_id'])
            return jsonify(session['client_id'])


@app.route('/server/operazione', methods=['GET'])
def operazione():
    if 'msg' in request.args:
        msg = request.args['msg']
        if msg == 'richiesta':
            operazione_attuale = session['lista_operazioni'].pop()
            session['id_oprazione_attuale'] = operazione_attuale['id']
            session['oprazione_attuale'] = operazione_attuale['op']
            return jsonify(session['oprazione_attuale'])
        if msg == 'soluzione' and 'risultato' in request.args:
            scritturaDB(['id_oprazione_attuale'], session['client_id'], request.args['risultato'])
            return jsonify(f"Grazie {session['client']}")



# lettura operazioni da db
def letturaDBOperazione(numClient):
    operazioni=[]
    db_connection = sqlite3.connect('db.db')
    db_cursor = db_connection.cursor()
    for row in db_cursor.execute(f'SELECT idOperazione, operazione FROM Operazioni '
                              f'WHERE idClient=="{numClient}" and risultato ISNULL'):
        operazioni.append({'id': row[0], 'op':row[1]})
    db_cursor.close()
    return operazioni

#scrittura db risultato operazione
def scritturaDB(id, idClient,risultato):
    db_connection = sqlite3.connect('db.db')
    db_cursor = db_connection.cursor()
    db_cursor.execute(f'UPDATE Operazioni '
                      f'SET risultato = {risultato} '
                      f'WHERE idOperazione=={id} and idClient=={idClient}')
    db_cursor.close()
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug='on')
