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
    try:
        cantVar = int(request.form.get('CantVar'))
    except:
        cantVar = 0

    
    return render_template('restricciones.html',metodo = metodo,cantVar = cantVar)

    

if __name__ == '__main__':
    app.run(debug=True)

