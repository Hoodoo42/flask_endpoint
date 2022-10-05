import mariadb
from flask import Flask, request
import json
import dbhelpers as dbh

app = Flask(__name__)

@app.get('/api/clients')
def get_client_info():
    results = dbh.make_api('CALL get_client_info')
    return results

@app.get('/api/loyal_clients')
def loyalty_points_filter():
    min_points = request.args.get('min_points')
    results = dbh.make_api('CALL points_filter(?)', [min_points])
    return results
    



app.run(debug=True)
