from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

latest_command = ""

@app.route('/command', methods=['POST'])
def handle_command():
    global latest_command
    data = request.get_json()
    command = data.get("command", "")
    print("Received command:", command)

    if command:
        latest_command = command
        return {'status': 'ok', 'received': command}, 200
    else:
        return {'status': 'error', 'message': 'No command received'}, 400

@app.route('/command', methods=['GET'])
def get_command():
    return jsonify({'command': latest_command}), 200

@app.route('/', methods=['GET'])
def get_status():
    return jsonify(status='running'), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
