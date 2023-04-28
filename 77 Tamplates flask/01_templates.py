from flask import Flask, render_template, request

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

# render_template()
# rendereizar la platilla 'mostrar.html'
# meterle variables o informacion a las platillas nombre=nombre


@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)
