from data.funciones.Ordenador import ordenador
from data.funciones.get_last_solutions import get_last_result
from data.funciones.valid_method import valid_method
from data.funciones.create_variable_names import create_variable_names
from data.metodos.simplex.SimplexMethod import SimplexMethod
from data.metodos.grafico.GraphicMethod import metodo_grafico
from data.metodos.simplex.TwoFases import Twofases
from flask import Flask, render_template, request, redirect, url_for, session, jsonify

# hacer funcion que use CantVar para agregar los X[] en name_variable


app = Flask(__name__)
# secret key para la sesion y el guardado de la informacion
app.secret_key = "1234566789"


# ruta principal
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/restricciones", methods=["POST"])
def restricciones():
    metodo = request.form.get("metodo")
    cantVar = request.form.get("CantVar")
    

    try:
        cantVar = int(request.form.get("CantVar"))
    except:
        cantVar = 0
    return render_template("restricciones.html", cantVar=cantVar, metodo=metodo)


@app.route("/resultados", methods=["POST"])
def resultados():
    metodo = request.form.get("metodo")
    min_max = request.form.get("min_max")
    cantVar = request.form.get("cantVar")
    igualdad = request.form.getlist("igualdades[]")
    igualdad.insert(0, "=")
    datos_variables = {}

    variable_standard = ["Z"]
    # hacer funcion que use CantVar para agregar los X[] en name_variable
    name_variable = create_variable_names(cant_var=cantVar)
    for key in request.form.keys():
        if key.startswith("x"):
            # getlist extrae todos los inputs con el mismo nombre (las filas añadidas)
            datos_variables[key] = request.form.getlist(key)
    # También capturamos los resultados (lo que está después del =)
    resultados = request.form.getlist("res[]")

    datos_variables["res[]"] = request.form.getlist("res[]")
    listaf = ordenador(datos_variables,metodo=='grafico')
    
    match (metodo):
        case "simplex":
            matrix, var_names, variable_standard,tipo_solucion = SimplexMethod(
                listaf,
                name_variable,
                igualdad,
                variable_standard,
                valid_method(min_max),
            )
            var_names.append("SOL")
            var_names.insert(0,"")
            soluciones = get_last_result(matrix=matrix)
            return render_template(
                "resultados_simplex.html",
                matrix=matrix,
                var_names=var_names,
                lista_standard = variable_standard,
                variable_standard=variable_standard[-1],
                soluciones=soluciones,
                min_max=min_max,
                tipo_solucion = tipo_solucion
                
            )
        case "dos-pasos":
            matrix_fase1, matrix_fase2, var_names,name_variable_second_fase,variable_standard,solucion,variable_standard_secondF = Twofases(
                listaf,
                name_variable,
                igualdad,
                variable_standard,
                valid_method(min_max),
                
            )
            
            var_names.append("SOL")
            name_variable_second_fase.append("SOL")
            var_names.insert(0,"")
            name_variable_second_fase.insert(0,"")
            if (solucion == "No Factible"):
                soluciones = get_last_result(matrix=matrix_fase1)
                return render_template(
                    "resultados_dos_fases.html",
                    matrix=matrix_fase1,#matriz de la primera fase(historico)
                    matrix_secondfase=[],#matriz de la segunda fase(historico)
                    var_names=var_names,#variables de la primera fase(con R)
                    var_second = name_variable_second_fase,#variables de la segunda fase
                    lista_standard = variable_standard,
                    variable_standard_secondF = variable_standard,
                    variable_standard=variable_standard[-1],#variables estandar para el resultado final
                    soluciones=soluciones,#valores de las soluciones para resultado final
                    min_max=min_max,#variable para saber si es minimizacion o maximizacion
                    solucion = solucion
                )
            else:
                soluciones = get_last_result(matrix=matrix_fase2)
                return render_template(
                    "resultados_dos_fases.html",
                    matrix=matrix_fase1,#matriz de la primera fase(historico)
                    matrix_secondfase=matrix_fase2,#matriz de la segunda fase(historico)
                    var_names=var_names,#variables de la primera fase(con R)
                    var_second = name_variable_second_fase,#variables de la segunda fase
                    lista_standard = variable_standard,
                    variable_standard_secondF = variable_standard_secondF,
                    variable_standard=variable_standard_secondF[-1],#variables estandar para el resultado final
                    soluciones=soluciones,#valores de las soluciones para resultado final
                    min_max=min_max,#variable para saber si es minimizacion o maximizacion
                    solucion = solucion
                )
        case 'grafico':
            is_min = valid_method(min_max)
            json_matrix = metodo_grafico(listaf,is_min,igualdad)
            return render_template(
                "resultados_grafico.html",
                json_matrix=json_matrix,
                min_max=min_max
                
            )


if __name__ == "__main__":
    app.run(debug=True)
