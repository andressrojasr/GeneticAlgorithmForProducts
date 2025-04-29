from flask import Blueprint, request, jsonify
import algorithm.algorithm as algorithm

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
    idCategory = data['idCategory']
    best, bestFit, ids = algorithm.initializeGenetic_int(nombre, volumen, poblacion, generaciones, volumenMaximo, alpha, idCategory)
    return jsonify({'Mejor combinación': best, "ids": ids, 'Mejor ganancia': bestFit}), 201