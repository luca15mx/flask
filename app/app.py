from contextlib import redirect_stderr
from distutils.log import debug
from pydoc import render_doc

from flask import Flask, request, redirect, url_for
from flask import render_template

app=Flask(__name__)

@app.before_request
def before_request():
    print("Antes de la petición")

@app.after_request
def after_request(response):
    print("Despues de la petición")
    return response

@app.route("/")
def index():
    # return "!Hola Mundo con Flask Debug Mode!"
    canes = ['Palomo', 'Perla', 'Juanito', 'Maya', 'Candy', 'Burbuja', 'Enzo', 'Dan', 'Beji', 'Sury', 'Joy', 'Pietro']
    data = {
        'titulo': 'Index',
        'bienvenida': 'Saludos!',
        'familia': canes,
        'familiares': len(canes)
    }
    return render_template("index.html", data=data)

@app.route("/vista")
def vista():
    return "Hola Vista"    

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data = {
        'titulo': 'contacto',
        'nombre': nombre,
        'edad': edad
    }
    return render_template('contacto.html', data=data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('Autos'))
    return "OK"

def pagina_no_encontrada(error):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)