from app import app
from app.version import APIVERSION
from flask import request
from flask.wrappers import Response


from app.dbManager import DbManager

#app = Flask(__name__)
dbm = DbManager()

@app.route("/")
def run():
    return f"API About Moving  v{APIVERSION} up and running!!"

if __name__ == "__main__":
    app.run(debug=True, port=6001)