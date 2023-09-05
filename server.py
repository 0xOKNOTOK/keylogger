#requires flask for running server, this is a simple REST API
# install via pip

from flask import Flask, jsonify, request

app = Flask(__name__)

logged_data = [
    {}
]

@app.route('/getdata')

def returnData():
    return jsonify(logged_data), 200


@app.route('/send', methods=['POST'])

def log_data():
    logged_data.append(request.get_json())
    return '', 204
    