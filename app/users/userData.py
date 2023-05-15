import datetime
import json
from app.dbManager import DbManager
from app.format import Format

class UsersData():
    format = Format()

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__() 
        self.db = DbManager()
        
    def addUser(self, inputjson):
        try:
            query = """INSERT INTO usuarios ( nombre , email, contrasena"""
            query = (
                query
                + f"""
                                )
                                VALUES (
                                    '{inputjson["nombre"]}',
                                    '{inputjson["email"]}',
                                    '{inputjson["contrasena"]}'
                                    )"""
            )
            self.db.execute(query)
        except Exception as e:
            print(e)
            return ({"message": "Insert failed, check log"}, 406)
        else:
            return ({"message": f"Added User"}, 200)

    def getUser(self, inputjson):
        try:
            query = f"""SELECT id, nombre, email
                        FROM usuarios 
                        WHERE nombre = '{inputjson["nombre"]}' """

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