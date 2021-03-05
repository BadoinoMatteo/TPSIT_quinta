from flask import Flask, jsonify, request
import sqlite3
app = Flask(__name__)

books={}

def gestioneDB(titolo):
    global books
    db_connection = sqlite3.connect('book.db')
    db_cursor = db_connection.cursor()
    for row in db_cursor.execute('SELECT * FROM libri WHERE nome = "titolo"') :
        print(row[0])
        books.update({'id': row[0], 'titolo': row[1], 'anno':row[2]})
    print(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    global books
    if  'name' in request.args :
        name = (str)(request.args['name'])
    else:
        return "error"

    result = []
    gestioneDB(name)
    for book in books:
        if books['name'] == name:
            result.append(book)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
