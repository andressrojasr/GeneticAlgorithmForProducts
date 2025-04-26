from flask import Flask
from flask_cors import CORS
from routes import register_blueprints

app = Flask(__name__)
CORS(app, origins="*", methods=["GET", "POST", "DELETE", "PUT"])

register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)
