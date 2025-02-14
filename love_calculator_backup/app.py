from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

def calcular_compatibilidad(nombre1, nombre2):
    
    letras_comunes = len(set(nombre1.lower()) & set(nombre2.lower()))
    compatibilidad = (letras_comunes * 10) + random.randint(0, 20)
    return min(compatibilidad, 100)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.json
    nombre1 = data.get('nombre1', '').strip()
    nombre2 = data.get('nombre2', '').strip()

    if not nombre1 or not nombre2:
        return jsonify({'error': 'Por favor, ingresa ambos nombres.'})

    porcentaje = calcular_compatibilidad(nombre1, nombre2)
    return jsonify({'nombre1': nombre1, 'nombre2': nombre2, 'porcentaje': porcentaje})

if __name__ == '__main__':
    app.run(debug=True)