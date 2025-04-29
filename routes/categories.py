from flask import Blueprint, request, jsonify
import controller.categories as c

categories_bp = Blueprint('categories', __name__, url_prefix='/category')

@categories_bp.route('/', methods=['GET'])
def getCategory():
    categorias = c.obtenerCategorias()    
    return jsonify(categorias), 200

@categories_bp.route('/', methods=['POST' , 'OPTIONS'] )
def createCategory():
    data = request.get_json()
    nombre = data['nombre']
    result = c.insertarCategoria(nombre)
    if result == True:
        return jsonify({'mensaje': 'Categoría creada exitosamente', 'data': data}), 201
    else:
        return jsonify({'error': f'Error al crear categoría , error.response ? error.response.data : error.message'}), 400

@categories_bp.route('/', methods=['PUT'])
def updateCategory():
    data = request.get_json()
    id = data['id']
    nombre = data['nombre']
    if not all([id, nombre]):
        return jsonify({"error": "Faltan datos requeridos"}), 400
    result = c.actualizarCategoria(id, nombre)
    if result == True:
        return jsonify({'mensaje': 'Categoría actualizada exitosamente', 'data': data}), 200
    else:
        return jsonify({'error': f'Error al actualizar categoría: {result}'}), 400

@categories_bp.route('/', methods=['DELETE'])
def deleteCategory():
    data = request.get_json()
    if not data or 'id' not in data:
        return jsonify({'error': 'ID no proporcionado'}), 400
    result = c.eliminarCategoria(data['id'])
    if result == True:
        return jsonify({'mensaje': 'Categoría eliminada exitosamente'}), 200
    else:
        return jsonify({'error': result}), 500
