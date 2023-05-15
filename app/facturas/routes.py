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