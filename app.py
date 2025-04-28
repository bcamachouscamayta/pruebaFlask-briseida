from flask import Flask
from flask import Flask, url_for
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

db = None

def dict_factory(cursor, row):
   """Arma un diccionario con los valores de la fila."""
   fields = [column[0] for column in cursor.description]
   return {key: value for key, value in zip(fields, row)}

def abrirConexion():
    global db
    db = sqlite3.connect("instance/datos.sqlite")
    db.row_factory = dict_factory

def cerrarConexion():

    global db
    db.close()
    db = None

@app.route("/test-db")
def testDB():
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*)FROM usuarios; ")
    res = cursor.fetchone()
    registros = res["cant"]
    cerrarConexion()
    return f"hay {registros}registros en la tabla de usuarios"

app = Flask(__name__)

@app.route('/hola/chau')
def hola():
##al lado de / se pone otro nombre opcional 
    return 'Hello, World!'
def chau():
    return'chau'

@app.route("/holaaa")
def salir():
    return "<p> chauuu</p>"

@app.route("/saludar/por-nombre/<string:nombre>")
def sxm(nombre):
    return f"<p>hola {nombre}</p>"

@app.route("/mostrar-datos-plantilla/<int:id>")
def datos_plantilla(id):
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELEC id,usuario, email FROM usuarios WHERE id = ?;", (id,))
    res = cursor.fetchone()
    cerrarConexion()
    usuario = None
    email = None
    if res != None:
        usuario=res['usuario']
        email=res['usuario']
    return render_template("datos2.html", id=id, usuario=usuario, email=email)