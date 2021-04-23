from flask import Flask, jsonify

app=Flask(__name__)


books=[
    {
    'id':0,
    'name': "libro1",
    'anno':2012},
    {
    'id':1,
    'name': "libro2",
    'anno':2021,
    }
]

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)