from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
from werkzeug.exceptions import abort

app = Flask(__name__)

# http://localhost:5000/


@app.route('/')
def inicio():
    app.logger.info(f'Entramos al path {request.path}')
    return 'Hola Mundo desde Flask.'


@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre}'


@app.route('/edad/<int:edad>')
def mostrar_edad(edad):
    return f'Tu edad es: {edad}'


@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)


# redireccionar con url_for()
@app.route('/redir/')
def redireccionar():
    return redirect(url_for('inicio'))
  
#manejo de errores
@app.route('/salir/')
def salir():
    return abort(404)
  
@app.errorhandler(404)
def pagina_no_encontrada(error):
  return render_template('error404.html', error=error), 404