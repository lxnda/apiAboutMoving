import datetime
import json
from app.format import Format

class ClientesData():
    format = Format()

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__() 
    
        
    def getUsersInformation(self, inputjson):
        try:
            query = f"""SELECT id, nombre, telefono, email, direccion, id_empresa
                        FROM clientes 
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
            return ({"data": output_json}, 200)