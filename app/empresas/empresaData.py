import datetime
import json
from app.dbManager import DbManager
from app.format import Format

class EmpresaData():
    format = Format()

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__() 
        self.db = DbManager()
        
    def addEmpresa(self, inputjson):
        try:
            query = """INSERT INTO empresa ( nombre , direccion, telefono, email, id_usuario"""
            query = (
                query
                + f"""
                                )
                                VALUES (
                                    '{inputjson["nombre"]}',
                                    '{inputjson["direccion"]}',
                                    {inputjson["telefono"]},
                                     '{inputjson["email"]}',
                                    {inputjson["id_usuario"]}
                                    )"""
            )
            self.db.execute(query)
        except Exception as e:
            print(e)
            return ({"message": "Insert failed, check log"}, 406)
        else:
            return ({"message": f"Added Empresa"}, 200)
