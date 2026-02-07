from data.funciones.Ordenador import ordenador
from data.funciones.valid_method import valid_method
from data.metodos.simplex.SimplexMethod import SimplexMethod
from data.metodos.simplex.TwoFases import Twofases
from flask import Flask, render_template, request, redirect, url_for, session,jsonify

#hacer funcion que use CantVar para agregar los X[] en name_variable


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
    
    try:
        cantVar = int(request.form.get('CantVar'))
    except:
        cantVar = 0
    return render_template('restricciones.html', cantVar=cantVar, metodo=metodo)

@app.route('/resultados', methods=['POST'])
def resultados():
    metodo = request.form.get('metodo')
    min_max = request.form.get('min_max')
    cantVar = request.form.get('CantVar')
    print(min_max)
    igualdad = request.form.getlist('igualdades[]')
    igualdad.insert(0,'=')
    datos_variables = {}

    variable_standard = ['Z']
    #hacer funcion que use CantVar para agregar los X[] en name_variable
    name_variable = ["Z","X1","X2"]
    for key in request.form.keys():
        if key.startswith('x'):
            # getlist extrae todos los inputs con el mismo nombre (las filas añadidas)
            datos_variables[key] = request.form.getlist(key)    
    # También capturamos los resultados (lo que está después del =)
    resultados = request.form.getlist('res[]')
    
    datos_variables['res[]'] = request.form.getlist('res[]')
    listaf = ordenador(datos_variables)
    
    match(metodo):
        case "simplex":
            matrix,var_names,variable_standard = SimplexMethod(listaf,name_variable,igualdad,variable_standard,valid_method(min_max))
            name_variable.append("SOL")
            return render_template('resultados.html',matrix=matrix,var_names=var_names,variable_standard=variable_standard)
        case "dos-pasos":
            matrix,var_names,variable_standard = Twofases(listaf,name_variable,igualdad,variable_standard,valid_method(min_max))
            name_variable.append("SOL")
            return render_template('resultados.html',matrix=matrix,var_names=var_names,variable_standard=variable_standard)
        case _:
            matrix,var_names,variable_standard = SimplexMethod(listaf,name_variable,igualdad,variable_standard,valid_method(min_max))
            name_variable.append("SOL")
            return render_template('resultados.html',matrix=matrix,var_names=var_names,variable_standard=variable_standard)
            
    

    

if __name__ == '__main__':
    app.run(debug=True)

