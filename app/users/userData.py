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
            query = """INSERT INTO usuarios ( nombre , email, contrasena, id_empresa"""
            query = (
                query
                + f"""
                                )
                                VALUES (
                                    '{inputjson["nombre"]}',
                                    '{inputjson["email"]}',
                                    '{inputjson["contrasena"]}',
                                    {inputjson["id_empresa"]},
                                    )"""
            )
            self.db.execute(query)
        except Exception as e:
            print(e)
            return ({"message": "Insert failed, check log"}, 406)
        else:
            return ({"message": f"Added User"}, 200)
