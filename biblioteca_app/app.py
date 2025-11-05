
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

libros = [
    {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry"},
    {"titulo": "1984", "autor": "George Orwell"},
    
    {"titulo": "El ingenioso hidalgo don Quijote de la Mancha", "autor": ""},
    {"titulo": "1605-1615", "autor": "Miguel de Cervantes"}
    
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/libros')
def libros_view():
    return render_template('libros.html', libros=libros)

@app.route('/agregar', methods=['GET','POST'])
def agregar():
    if request.method == 'POST':
        titulo=request.form['titulo']
        autor=request.form['autor']
        libros.append({"titulo":titulo,"autor":autor})
        return redirect(url_for('libros_view'))
    return render_template('agregar.html')

@app.route('/arriendo')
def arriendo():
    return render_template('arriendo.html', libros=libros)

if __name__ == '__main__':
    app.run(debug=True)
