import datetime 
import json
from decimal import *
class Format:

    def __init__(self):
        pass

    def formatListToJsonList(self,list):

        response = []
        column_names = list[0] 

        for fila in list[1:]:
            jsonStructure = {}
            for column in range(0, len(column_names)):
                if isinstance(fila[column], Decimal):
                    jsonStructure[column_names[column]] = float(fila[column])
                elif isinstance(fila[column], datetime.date) :
                    jsonStructure[column_names[column]] = str(fila[column])
                elif "{" in str(fila[column]):
                    jsonStructure[column_names[column]] = json.loads(fila[column])
                else: 
                    jsonStructure[column_names[column]] = fila[column]
            response.append(jsonStructure)
        
        return response

    def formatFileteredListToJson(self,list, column_names):

        response = []

        for fila in list[0:]:
            json = {}
            for column in range(1, len(column_names)):
                if isinstance(fila[column], Decimal):
                    json[column_names[column]] = float(fila[column])
                elif isinstance(fila[column], datetime.date):
                    json[column_names[column]] = str(fila[column])
                else: 
                    json[column_names[column]] = fila[column]
            response.append(json)
        
        return response
