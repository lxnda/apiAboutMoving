import datetime
import json
from app.format import Format

class ClientesData():
    format = Format()

    # ----------------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__()
        
    def getUserInformation(self, inputjson):
        return ({"message": f"Added"}, 200)