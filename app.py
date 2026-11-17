from flask import Flask, jsonify

app = Flask(__name__)                          # creates flask application instance
@app.route('/health', methods= ['GET'])        # @app.route() defines the API endpoints and methods=['GET'] allows GET requests.
def health():
    return jsonify({"status": "running"})      # jasonify returns a json response.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)         # app.run starts the development server and host='0.0.0.0' makes the application accessible outside it's container.
