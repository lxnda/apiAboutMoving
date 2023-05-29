import datetime
import json
from app.dbManager import DbManager
from app.format import Format

class MudanzaData():
    format = Format()

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__() 
        self.db = DbManager()
        
    def addMudanza(self, inputjson):
        try:
            query = """INSERT INTO mudanzas ( fecha , direccion_origen, direccion_destino,
                       descripcion, tipo, total_mudanza ,id_cliente """
            query = (
                query
                + f"""
                                )
                                VALUES (
                                    '{inputjson["fecha"]}',
                                    '{inputjson["direccion_origen"]}',
                                    '{inputjson["direccion_destino"]}',
                                    '{inputjson["descripcion"]}',
                                    '{inputjson["tipo"]}',
                                    {inputjson["total_mudanza"]},
                                    {inputjson["id_cliente"]}
                                    )"""
            )
            self.db.execute(query)
        except Exception as e:
            print(e)
            return ({"message": "Insert failed, check log"}, 406)
        else:
            return ({"message": f"Added User"}, 200)


    def getMudanza(self, inputjson):
        try:
            query = f"""SELECT id,fecha , direccion_origen, direccion_destino,
                        descripcion, tipo
                        FROM mudanzas 
                        WHERE id_cliente = {inputjson["id_cliente"]} """

            data = self.db.read(query)
            if len(data) == 0:
                return ({"message": "No data found"}, 406)
            else:
                output_json = self.format.formatListToJsonList(data)
        except Exception as e:
            print(e)
            return ({"message": "failed, check log"}, 406)
        else:
            return ({"data": output_json}, 200)
        
        
        
    def getMudanzas(self, inputjson):
        try:
            query = f"""SELECT m.id, m.fecha ,m.direccion_origen, m.direccion_destino,
                        m.descripcion, m.tipo, m.total_mudanza, c.nombre , c.id
                        FROM mudanzas as m  JOIN  clientes as c ON c.id = m.id_cliente 
                        WHERE c.id_empresa = {inputjson["id_empresa"]} """

            data = self.db.read(query)
            if len(data) == 0:
                return ({"message": "No data found"}, 406)
            else:
                output_json = self.format.formatListToJsonList(data)
        except Exception as e:
            print(e)
            return ({"message": "failed, check log"}, 406)
        else:
            return ({"data": output_json}, 200)   