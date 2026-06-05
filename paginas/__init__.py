from flask import Flask
from db import get_connection
from paginas.inicio import inicio_bp
from paginas.contact import contact_bp
from paginas.shop import shop_bp
from paginas.edicion1 import edicion1_bp
from paginas.edi1 import edi1_bp
from paginas.entidades import entidades_bp
import os

def create_app():
    #'..'
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'templates'))
    app = Flask(__name__, template_folder=template_dir)
    app.register_blueprint(inicio_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(shop_bp)
    app.register_blueprint(edicion1_bp)
    app.register_blueprint(edi1_bp)
    app.register_blueprint(entidades_bp)

    return app
