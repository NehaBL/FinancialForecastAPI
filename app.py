from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/forecast', methods=['GET'])
def forecast():
    return jsonify({'message': 'Financial Forecast API working!'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # use the port Render provides
    app.run(host='0.0.0.0', port=port)         # bind to 0.0.0.0

