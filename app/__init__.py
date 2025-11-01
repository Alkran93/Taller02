from flask import Flask
from .routes import routes
import os

def create_app():
    # Buscar la carpeta 'templates' fuera del módulo app
    base_dir = os.path.dirname(os.path.dirname(__file__))
    template_dir = os.path.join(base_dir, 'templates')

    app = Flask(__name__, template_folder=template_dir)
    app.register_blueprint(routes)
    return app
