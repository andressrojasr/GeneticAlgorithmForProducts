from flask import Blueprint, request, jsonify
from flask_cors import cross_origin, CORS
import algorithm.genetic as genetic

algorithm_bp = Blueprint('algorithm', __name__, url_prefix='/algorithm')


@algorithm_bp.route('/', methods=['OPTIONS'],strict_slashes=False)


@algorithm_bp.route('/', methods=['POST', 'OPTIONS'])
def createProduct():
    if request.method == 'OPTIONS':
        response = jsonify({})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        return response,200
    
    data = request.get_json()
    nombre = data['porcentajeCruce']
    volumen = data['porcentajeMutacion']
    poblacion = data['poblacion']
    generaciones = data['generaciones']
    volumenMaximo = data['volumenMaximo']
    alpha = data['alpha']
    productosSeleccionados = data['productosSeleccionados']
    best, bestFit = genetic.initializeGenetic(nombre, volumen, poblacion, generaciones, volumenMaximo, alpha,productosSeleccionados)
    print(data)
    return jsonify({'Mejor combinación': best, 'Mejor ganancia': bestFit}), 201