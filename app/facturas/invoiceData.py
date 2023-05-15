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
