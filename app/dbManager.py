# -*- coding: utf-8 -*-
import pymssql
import json
class DbManager:

    def __init__(self):
        
        self.server = '85.10.205.173:3306'
        self.database = 'aboutmoving'
        self.username = 'lauralpz' 
        self.password = "Linda2001"

    def read(self, query):
        #crea una conexion a la base de datos definida en el __init__ que ejecute una query que lea datetime como string

        cnxn = pymssql.connect(host=self.server, user=self.username, password=self.password, database=self.database)        
        cursor = cnxn.cursor()
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lindalpz:Linda2001@db4free.net/tienda_bdd'
        
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            column_names = [item[0] for item in cursor.description]

            data = []

            data.append(column_names)
            
            for row in rows:
                dataSlice = []
                for r in row:
                    dataSlice.append(r)
            
                data.append(dataSlice)

            return data
        
        except Exception as e:
            
            print("ERROR executing query: " + str(e))
            return ("ERROR reading database: " + str(e))

        finally:

            cursor.close()
            cnxn.close()
    

            cnxn.close()

    def readJSON(self, table):

        cnxn = pymssql.connect(host=self.server, user=self.username, password=self.password, database=self.database)        
        cursor = cnxn.cursor()

        query = f"SELECT * FROM {table} FOR JSON AUTO"

        try:
            cursor.execute(query)
            rows = cursor.fetchall()

            return json.loads(rows[0][0])
        
        except Exception as e:
            
            print("ERROR executing query: " + str(e))
            return ("ERROR reading database: " + str(e))

        finally:

            cursor.close()
            cnxn.close()
    

            cnxn.close()

    def readJSON2(self, query):
        cnxn = pymssql.connect(host=self.server, user=self.username, password=self.password, database=self.database)        
        cursor = cnxn.cursor()

        try:
            cursor.execute(query)
            rows = cursor.fetchall()

            return json.loads(rows[0][0])
        
        except Exception as e:
            
            print("ERROR executing query: " + str(e))
            return ("ERROR reading database: " + str(e))

        finally:

            cursor.close()
            cnxn.close()


    def execute(self, query):
        
        cnxn = pymssql.connect(host=self.server, user=self.username, password=self.password, database=self.database, charset="CP936")        
        cursor = cnxn.cursor()

        try:

            cursor.execute(query)
            cnxn.commit()

            return cursor.rowcount

        except Exception as e:

            print(f"ERROR executing query: {e}")
            raise(f"ERROR executing query: {e}")
            

        finally:

            cursor.close()
            cnxn.close()