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