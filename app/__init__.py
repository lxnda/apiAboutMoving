from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
from app import routes

from app.clientes import routes
from app.users import routes
from app.empresas import routes
from app.facturas import routes
from app.mudanzas import routes