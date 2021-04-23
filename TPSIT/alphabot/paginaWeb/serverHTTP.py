from flask import Flask, render_template, request
import AlphaBot
app=Flask(__name__)
alphabot = AlphaBot.AlphaBot()
alphabot.stop()

@app.route('/index/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        button=str(request.form['direzione'])
        direzione(alphabot, button)
    return render_template('index.html')

def direzione(alphabot, comando):
    switcher = {
        "FW": alphabot.forward,
        "BW": alphabot.backward,
        "RT": alphabot.right,
        "LT": alphabot.left,
        "STOP": alphabot.stop
    }
    switcher[comando]()

if __name__ == '__main__':
    app.run(host='192.168.1.31', debug='on')

