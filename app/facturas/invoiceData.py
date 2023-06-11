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
            fecha = str(inputjson["fecha"] )
            fecha_sin_guiones = fecha.replace('-', '')
            idconcat= "F" + str(inputjson["idempresa"]) + fecha_sin_guiones
            query = """INSERT INTO facturas ( fecha , total, idempresa, idfactura, nombrecliente, descripcion"""
            query = (
                query
                + f"""
                                )
                                VALUES (
                                    '{inputjson["fecha"]}',
                                    {inputjson["total"]},
                                    {inputjson["idempresa"]},
                                    '{idconcat}',
                                    '{inputjson["nombrecliente"]}',
                                    '{inputjson["descripcion"]}'
                                    )"""
            )
            self.db.execute(query)
        except Exception as e:
            print(e)
            return ({"message": "Insert failed, check log"}, 406)
        else:
            return ({"message": f"Added Invoice"}, 200)


    def getInvoice(self, id_empresa):
        try:
            query = f"""SELECT id, fecha, total, idfactura, nombrecliente,descripcion
                        FROM facturas 
                        WHERE idempresa = {id_empresa} """

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
        

    def deleteInvoice(self, inputjson):
        try:
             # Eliminar registros relacionados en la tabla "mudanzas"
            query_invoice = """DELETE FROM facturas
                                WHERE id = '{}'""".format(inputjson["id"])
            self.db.execute(query_invoice)


            return ({"message": "Factura deleted successfully"}, 200)
        except Exception as e:
            print(e)
            return ({"message": "Failed to delete Factura"}, 406)
