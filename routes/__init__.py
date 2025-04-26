from .products import products_bp
from .categories import categories_bp
from .geneticAlgorithm import algorithm_bp

def register_blueprints(app):
    app.register_blueprint(products_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(algorithm_bp)