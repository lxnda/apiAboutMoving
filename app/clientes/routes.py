from app import app
from app.clientes.clientesData import ClientesData
from flask import request
from flask.wrappers import Response
import requests
import json

dm = ClientesData()

@app.route("/getUserInformation", methods = ['POST'])
def getUserInformation():

    inputJson = request.json
    result = dm.getUserInformation(inputJson)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)