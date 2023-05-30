from app import app
from app.users.userData import UsersData
from flask import request
from flask.wrappers import Response
import requests
import json

dm = UsersData()

@app.route("/addUser", methods = ['POST'])
def addUser():

    inputJson = request.json
    result = dm.addUser(inputJson)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)

@app.route("/getUser", methods = ['POST'])
def getUser():

    inputJson = request.json
    result = dm.getUser(inputJson)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)

@app.route("/verificarUser", methods = ['POST'])
def verificarUser():

    inputJson = request.json
    result = dm.verificarUser(inputJson)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)

