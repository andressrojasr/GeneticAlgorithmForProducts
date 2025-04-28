from flask import Blueprint, request, jsonify
import algorithm.algorithm as algorithm

algorithm_bp = Blueprint('algorithm', __name__, url_prefix='/algorithm')


@algorithm_bp.route('/', methods=['POST'])
def createProduct():
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