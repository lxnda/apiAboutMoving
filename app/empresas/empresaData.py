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
        
    def addEmpresa(self, idUser ,inputjson):
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
                                    {idUser}
                                    )"""
            )
            self.db.execute(query)
        except Exception as e:
            print(e)
            return ({"message": "Insert failed, check log"}, 406)
        else:
            return ({"message": f"Added Empresa"}, 200)

    def getEmpresa(self, id_empresa):
        try:
            query = f"""SELECT id, nombre, direccion, telefono, email, id_usuario
                        FROM empresa 
                        WHERE id = {id_empresa} """

            data = self.db.read(query)
            if len(data) == 1:
                return ({"message": "No data found"}, 406)
            else:
                
                output_json = self.format.formatListToJsonList(data)
        except Exception as e:
            print(e)
            return ({"message": "failed, check log"}, 406)
        else:
            return output_json