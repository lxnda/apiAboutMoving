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