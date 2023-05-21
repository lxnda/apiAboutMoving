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


    def getClientes(self, id_empresa):
        try:
            query = f"""SELECT  id,nombre, telefono, email, direccion
                        FROM [clientes] 
                        WHERE id_empresa = {id_empresa} """

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
        
    def updateClientes(self, inputjson):
        try:
            query = """UPDATE clientes
                    SET nombre = '{}', direccion = '{}', telefono = '{}', email = '{}'
                    WHERE id_empresa = {} AND id = '{}'""".format(
                        inputjson["nombre"],
                        inputjson["direccion"],
                        inputjson["telefono"],
                        inputjson["email"],
                        inputjson["id_empresa"],
                        inputjson["id"]
                    )
            self.db.execute(query)
            return ({"message": "Cliente updated successfully"}, 200)
        except Exception as e:
            print(e)
            return ({"message": "Failed to update Cliente"}, 406)
    
    def deleteClientes(self, inputjson):
        try:
            # Eliminar registros relacionados en la tabla "mudanzas"
            query_mudanzas = """DELETE FROM mudanzas
                                WHERE id_cliente = '{}'""".format(inputjson["id"])
            self.db.execute(query_mudanzas)

            # Eliminar el cliente de la tabla "clientes"
            query_clientes = """DELETE FROM clientes
                                WHERE id_empresa = {} AND id = '{}'""".format(
                                    inputjson["id_empresa"],
                                    inputjson["id"]
                                )
            self.db.execute(query_clientes)

            return ({"message": "Cliente deleted successfully"}, 200)
        except Exception as e:
            print(e)
            return ({"message": "Failed to delete Cliente"}, 406)
        