from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_api():
    data = {
        'message': 'Hello, World!'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify({'message': f'Hello, {name}!'})

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.json
    return jsonify({'you_sent': data})
