from app import app
from app.clientes.clientesData import ClientesData
from flask import request
from flask.wrappers import Response
import requests
import json

dm = ClientesData()


@app.route("/addClientes", methods = ['POST'])
def addClientes():

    inputJson = request.json
    result = dm.addClientes(inputJson)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)

@app.route("/getClientes", methods = ['POST'])
def getClientes():

    inputJson = request.json
    result = dm.getClientes(inputJson)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)