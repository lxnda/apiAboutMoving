import datetime
import json
from app.dbManager import DbManager
from app.format import Format

class ClientesData():
    format = Format()

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__() 
        self.db = DbManager()
    

    def addClientes(self, inputjson):
        try:
            query = """INSERT INTO clientes ( nombre , direccion, telefono, email, id_empresa"""
            query = (
                query
                + f"""
                                )
                                VALUES (
                                    '{inputjson["nombre"]}',
                                    '{inputjson["direccion"]}',
                                    {inputjson["telefono"]},
                                     '{inputjson["email"]}',
                                    {inputjson["id_empresa"]}
                                    )"""
            )
            self.db.execute(query)
        except Exception as e:
            print(e)
            return ({"message": "Insert failed, check log"}, 406)
        else:
            return ({"message": f"Added Cliente"}, 200)


    def getClientes(self, inputjson):
        try:
            query = f"""SELECT  nombre, telefono, email, direccion
                        FROM [clientes] 
                        WHERE id_empresa = {inputjson["id_empresa"]} """

            data = self.db.read(query)
            if len(data) == 0:
                return ({"message": "No data found"}, 406)
            else:
                output_json = self.format.formatListToJsonList(data)
        except Exception as e:
            print(e)
            return ({"message": "failed, check log"}, 406)
        else:
            return (output_json, 200)