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

@app.route("/getClientes", methods = ['GET'])
def getClientes():
    id_empresa = request.args.get('id_empresa')
    result = dm.getClientes(id_empresa)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)

@app.route("/updateClientes", methods = ['PUT'])
def updateClientes():
    inputJson = request.json
    result = dm.updateClientes(inputJson)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)

@app.route("/deleteClientes", methods = ['DELETE'])
def deleteClientes():
    inputJson = request.json
    result = dm.deleteClientes(inputJson)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)

