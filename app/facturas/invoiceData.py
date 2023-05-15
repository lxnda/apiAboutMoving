import datetime
import json
from app.dbManager import DbManager
from app.format import Format

class InvoiceData():
    format = Format()

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__() 
        self.db = DbManager()
        
    def addInvoice(self, inputjson):
        try:
            query = """INSERT INTO facturas ( fecha , total, id_mudanza"""
            query = (
                query
                + f"""
                                )
                                VALUES (
                                    '{inputjson["fecha"]}',
                                    {inputjson["total"]},
                                    {inputjson["id_mudanza"]}
                                    )"""
            )
            self.db.execute(query)
        except Exception as e:
            print(e)
            return ({"message": "Insert failed, check log"}, 406)
        else:
            return ({"message": f"Added Invoice"}, 200)
        
    def getInvoice(self, inputjson):
        try:
            query = f"""SELECT id, fecha, total
                        FROM facturas 
                        WHERE id_mudanza = {inputjson["id_mudanza"]} """

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
