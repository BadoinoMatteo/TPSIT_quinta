from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app=Flask(__name__)


def validate(username, password):
    accesso=False
    db_connection = sqlite3.connect('db.db')
    db_cursor = db_connection.cursor()
    listaUsername = []
    usr=db_cursor.execute('SELECT username FROM credenziali')
    for row in usr.fetchall():
        listaUsername.append(row[0])
    print(listaUsername)
    listaPassword = []
    psw=db_cursor.execute('SELECT password FROM credenziali')
    for riga in psw.fetchall():
        listaPassword.append(riga[0])
    print(listaPassword)
    if username in listaUsername:
        print("uguali")
        indice=listaUsername.index(username)
        print(indice)
    if password in listaPassword and listaPassword.index(password)==indice:
        print("uguali")
        accesso=True
    print(accesso)
    return accesso


@app.route('/index/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = str(request.form['username'])
        print(username)
        password = str(request.form['password'])
        print(password)
        ret = validate(username, password)
        print(ret)
        if ret==True:
            return render_template('accesso.html')
    return render_template('index.html')

def secret():
    return "this is a secret page"

if __name__ == '__main__':
    app.run(debug=True)