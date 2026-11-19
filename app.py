from flask import Flask, jsonify
from db import get_connection
import os
import psycopg
from psycopg.rows import dict_row

app = Flask(__name__)                          # creates flask application instance
@app.route('/getUsers', methods= ['GET'])      # @app.route() defines/registers the API endpoints and methods=['GET'] allows GET requests.
def getUsers():
    connection = get_connection()
    cursor = connection.cursor(row_factory=dict_row)  # we use dict_row to get the result set as a list of dictionaries, where each dictionary represents a row and the keys are the column names.
    cursor.execute("select id, username, email from users")
    result = cursor.fetchall()
    return result                              # jasonify returns a json response.

if __name__ == '__main__':                     # we use this to check if the script is being run directly or imported as a module. If it is being run directly, the code inside the if block will be executed, in this case server will start.
    app.run(host='0.0.0.0', port=5050)         # app.run starts the development server and host='0.0.0.0' makes the application accessible outside it's container.