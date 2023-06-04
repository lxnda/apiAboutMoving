from app import app
from app.mudanzas.mudanzaData import MudanzaData
from flask import request
from flask.wrappers import Response
import requests
import json

dm = MudanzaData()

@app.route("/addMudanza", methods = ['POST'])
def addMudanza():

    inputJson = request.json
    result = dm.addMudanza(inputJson)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)


@app.route("/updateMudanza", methods = ['PUT'])
def updateMudanza():

    inputJson = request.json
    result = dm.updateMudanza(inputJson)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)

@app.route("/getMudanza", methods = ['POST'])
def getMudanza():

    inputJson = request.json
    result = dm.getMudanza(inputJson)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)

@app.route("/getMudanzas", methods = ['GET'])
def getMudanzas():
    id_empresa = request.args.get('id_empresa')
    result = dm.getMudanzas(id_empresa)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)

@app.route("/deleteMudanza", methods = ['DELETE'])
def deleteMudanza():
    inputJson = request.json
    result = dm.deleteMudanza(inputJson)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)