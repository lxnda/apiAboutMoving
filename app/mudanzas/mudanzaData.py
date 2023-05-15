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
                       descripcion, tipo, id_cliente """
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
                                    {inputjson["id_cliente"]}
                                    )"""
            )
            self.db.execute(query)
        except Exception as e:
            print(e)
            return ({"message": "Insert failed, check log"}, 406)
        else:
            return ({"message": f"Added User"}, 200)
