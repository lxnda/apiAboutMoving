from flask import Flask

app = Flask(__name__)

from app import routes

from app.clientes import routes
from app.users import routes
