from flask import Flask

app = Flask(__name__)


@app.route('/hola/chau')
def hola():
##al lado de / se pone otro nombre opcional 
    return 'Hello, World!'
def chau():
    return'chau'
