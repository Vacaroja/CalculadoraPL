from data.funciones.Ordenador import ordenador
from flask import Flask, render_template, request, redirect, url_for, session,jsonify


app = Flask(__name__)
#secret key para la sesion y el guardado de la informacion
app.secret_key = '1234566789'


#ruta principal
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/restricciones', methods=['POST'])
def restricciones():
    metodo = request.form.get('metodo')
    cantVar = request.form.get('CantVar')
    print(cantVar)
    print(metodo)
    try:
        cantVar = int(request.form.get('CantVar'))
    except:
        cantVar = 0
    return render_template('restricciones.html', cantVar=cantVar, metodo=metodo)

@app.route('/resultados', methods=['POST'])
def resultados():
    metodo = request.form.get('metodo')
    cantVar = request.form.get('CantVar')
    datos_variables = {}
    for key in request.form.keys():
        if key.startswith('x'):
            # getlist extrae todos los inputs con el mismo nombre (las filas añadidas)
            datos_variables[key] = request.form.getlist(key)    
    # También capturamos los resultados (lo que está después del =)
    resultados = request.form.getlist('res[]')
    datos_variables['res'] = request.form.getlist('res[]') 
    listaf = ordenador(datos_variables)
    for e in listaf:
        print(e)
    

    print(f"Variables capturadas: {datos_variables}")
    print(f"Resultados (Sol): {resultados}")

    print("Datos recibidos correctamente")
    
    return render_template('resultados.html')

    

if __name__ == '__main__':
    app.run(debug=True)

