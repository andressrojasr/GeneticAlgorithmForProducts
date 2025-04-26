from flask import Blueprint, request, jsonify
import controller.products as c

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/', methods=['GET'])
def getProduct():
    productos = c.obtenerProductos()    
    return jsonify(productos), 200

@products_bp.route('/', methods=['POST'])
def createProduct():
    data = request.get_json()
    nombre = data['nombre']
    volumen = data['volumen']
    ganancia = data['ganancia']
    idCategoria = data['idCategoria']
    url = data['url']
    result = c.insertarProducto(nombre, volumen, ganancia, idCategoria, url)
    if result == True:
        return jsonify({'mensaje': 'Producto creado exitosamente', 'data': data}), 201
    else:
        return jsonify({'error': f'Error al crear el producto {result}'}), 400

@products_bp.route('/', methods=['PUT'])
def updateProduct():
    data = request.get_json()
    id = data['id']
    nombre = data['nombre']
    volumen = data['volumen']
    ganancia = data['ganancia']
    idCategoria = data['idCategoria']
    url = data['url']
    if not all([id, nombre, volumen, ganancia, idCategoria, url]):
        return jsonify({"error": "Faltan datos requeridos"}), 400
    result = c.actualizarProducto(id, nombre, volumen, ganancia, idCategoria, url)
    if result == True:
        return jsonify({'mensaje': 'Producto actualizado exitosamente', 'data': data}), 200
    else:
        return jsonify({'error': f'Error al actualizar el producto: {result}'}), 400

@products_bp.route('/', methods=['DELETE'])
def deleteProduct():
    data = request.get_json()
    id = data['id']
    if not data or 'id' not in data:
        return jsonify({'error': 'ID no proporcionado'}), 400
    result = c.eliminarProducto(id)
    if result == True:
        return jsonify({'mensaje': 'Producto eliminado exitosamente'}), 200
    else:
        return jsonify({'error': result}), 500
