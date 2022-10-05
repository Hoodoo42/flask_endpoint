import mariadb
from flask import Flask
import json
import dbhelpers as dbh

app = Flask(__name__)

@app.get('/api/clients')
def get_client_info():
    results = dbh.make_api('CALL get_client_info')
    return results


app.run(debug=True)