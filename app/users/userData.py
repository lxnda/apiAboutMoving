import datetime
import json
from app.dbManager import DbManager
from app.format import Format
from app.empresas.empresaData import EmpresaData

dm = EmpresaData()

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
            query = f"""SELECT id
                        FROM usuarios 
                        WHERE email = '{inputjson["email"]}' """
            
            idUser=self.db.read(query)


            dm.addEmpresa(idUser[1][0], inputjson)
           
        except Exception as e:
            print(e)
            return ({"message": "Insert failed, check log"}, 406)
        else:
            return ({"message": f"Added User"}, 200)

    def getUser(self, inputjson):
        try:
            query = f"""SELECT id 
                        FROM empresa 
                        WHERE email = '{inputjson["email"]}' """

            data = self.db.read(query)
            if len(data) == 0:
                return ({"message": "No data found"}, 406)
            else:
                output_json = data[1][0]

        except Exception as e:
            print(e)
            return ({"message": "failed, check log"}, 406)
        else:
            return ({"id": output_json}, 200)
        
    def verificarUser(self, inputjson):
        try:
            query = f"""SELECT id 
                        FROM usuarios 
                        WHERE email = '{inputjson["email"]}' 
                        AND contrasena = '{inputjson["contrasena"]}' """

            data = self.db.read(query)
            if len(data[1:]) == 0:
                response = False
            else:
                response = True

        except Exception as e:
            print(e)
            return ({"message": "failed, check log"}, 406)
        else:
            return (response, 200)
