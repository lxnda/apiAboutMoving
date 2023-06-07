from app import app
from app.facturas.invoiceData import InvoiceData
from flask import request
from flask.wrappers import Response
import requests
import json

dm = InvoiceData()

@app.route("/addInvoice", methods = ['POST'])
def addInvoice():

    inputJson = request.json
    result = dm.addInvoice(inputJson)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)

@app.route("/getInvoice", methods = ['GET'])
def getInvoice():
    id_empresa = request.args.get('id_empresa')
    result = dm.getInvoice(id_empresa)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)

@app.route("/deleteInvoice", methods = ['DELETE'])
def deleteInvoice():
    inputJson = request.json
    result = dm.deleteInvoice(inputJson)

    message = result[0]
    returnCode = result[1]

    return Response(json.dumps(message), returnCode)