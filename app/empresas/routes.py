from app import app
from app.empresas.empresaData import EmpresaData
from flask import request
from flask.wrappers import Response
import requests
import json

dm = EmpresaData()

@app.route("/addEmpresa", methods = ['POST'])
def addEmpresa():

    inputJson = request.json
    result = dm.addEmpresa(inputJson)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)

@app.route("/getEmpresa", methods = ['POST'])
def getEmpresa():

    inputJson = request.json
    result = dm.getEmpresa(inputJson)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)