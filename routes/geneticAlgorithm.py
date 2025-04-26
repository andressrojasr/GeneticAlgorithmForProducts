from flask import Blueprint, request, jsonify
import algorithm.genetic as genetic

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
    best, bestFit = genetic.initializeGenetic(nombre, volumen, poblacion, generaciones, volumenMaximo, alpha)
    return jsonify({'Mejor combinación': best, 'Mejor ganancia': bestFit}), 201