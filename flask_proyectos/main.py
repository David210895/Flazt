from flask import Flask
from flask import request
from flask import render_template

#asignacion de aplicacion
app = Flask(__name__,template_folder="templates_codigo")
#decorador
@app.route('/')
def login():
    return "Esta es mi pagina de perritos tecsup codiGO"

@app.route('/perritos')
def perritos():
    return "Esta es la seccion perrito"

@app.route('/clientes')
def clientes():
    param = request.args.get("Usuario","parametro usuario vacio")
    param2 = request.args.get("Clave","parametro clave vacio")
    return "El cliente es: {},{}".format(param,param2)

@app.route('/usuario')
@app.route('/usuario/<codigo>')
@app.route('/usuario/<codigo>/<int:valor>')
def usuarios(codigo="Valor 0 por defecto ",valor=0):
    return "Los datos del usuario son : {} {}".format(codigo,valor)

@app.route('/front')
def index():
    return render_template('index.html')

@app.route('/frontags')
@app.route('/frontags/<curso>')
def cursos(curso="Flask"):
    edadmascota = 12
    mascotas = ['BOBY','PLUTO','CHOCOLATE']
    return render_template('mascotas.html',enviar=curso,edad=edadmascota,lista=mascotas)

@app.route('/principalportal')
def print():
    return render_template('principal.html')

@app.route('/formulario')
@app.route('/formulario/<nombre>')
def prin(nombre="tecsup"):
    return render_template('formulario.html',valor= nombre)


if __name__ == '__main__':
    app.run( debug = True, port = 8000)
