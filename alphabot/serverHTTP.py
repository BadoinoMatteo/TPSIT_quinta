import sqlite3
import flask
from flask import jsonify, request, render_template

app = flask.Flask(__name__)

"""
end: smartlab - start: info3
end: info1 - start: aula3.0
end: info2 - start: info1
end: info3 - start: aula3.0
"""


# http://127.0.0.1:5000/api/v1/resources/path?end=...&&start=...
@app.route('/api/v1/resources/path', methods=['GET'])
def api_id():
    app.logger.info(request.args)
    if 'end' in request.args and 'start' in request.args:
        end = request.args['end']
        start = request.args['start']
        app.logger.info(f"start: {start} - end: {end}")
        percorso = db_query_path(end, start)
        return jsonify(percorso)
    return render_template("index.html")

# http://127.0.0.1:5000/api/v1/resources/db?lato=...&&date=...
@app.route('/api/v1/resources/db', methods=['GET'])
def sensore():
    app.logger.info(request.args)
    print("dato arrivato")
    if 'lato' in request.args and 'date' in request.args:
        lato=str(request.args['lato'])
        date=str(request.args['date'])
        print(lato + date)
        db_query_sensore(lato, date)
    return render_template("index.html")




def db_query_path(end, start):
    db_connection = sqlite3.connect('percorsi.db')
    db_cursor = db_connection.cursor()
    print(
        f'SELECT percorsi.percorso FROM percorsi WHERE percorsi.id = (SELECT inizio_fine.id_percorso '
        f'FROM inizio_fine WHERE inizio_fine.id_end = (SELECT luoghi.id FROM luoghi '
        f'WHERE luoghi.nome = "{end}") AND inizio_fine.id_start = '
        f'(SELECT luoghi.id FROM luoghi WHERE luoghi.nome = "{start}"));')
    percorso = []
    for row in db_cursor.execute(f'SELECT percorsi.percorso FROM percorsi WHERE percorsi.id = '
                                 f'(SELECT inizio_fine.id_percorso FROM inizio_fine WHERE '
                                 f'inizio_fine.id_end = '
                                 f'(SELECT luoghi.id FROM luoghi WHERE luoghi.nome = "{end}") '
                                 f'AND inizio_fine.id_start = (SELECT luoghi.id FROM luoghi '
                                 f'WHERE luoghi.nome = "{start}"));'): percorso.append({'percorso': row[0]})
    db_connection.close()
    return percorso

def db_query_sensore(lato,date):
    db_connection = sqlite3.connect('percorsi.db')
    db_cursor = db_connection.cursor()
    esito=db_cursor.execute(f'INSERT INTO Sensore ("lato","data") VALUES ("{lato}", "{date}")')
    db_cursor.execute(f"COMMIT;")
    print(esito)


if __name__ == '__main__':
    app.run(host='192.168.43.90', debug='on')