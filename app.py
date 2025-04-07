from flask import Flask
from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def main():
    url_ekisde = url_for("ekisde")
    url_ekisde = url_for("ekisde")
    url_ekisde = url_for("ekisde")

return f"""
<a href="{url_ekisde}>lol</a>
<br>
<a href="{url_ekisde}>lol</a>
<br>
<a href="{url_ekisde}>lol</a>

"""



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
