# server.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# بدل latest_command، نستخدم قائمة تخزين مؤقتة للأوامر
command_queue = []

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.get_json()
    command = data.get("command", "").strip()
    if command:
        command_queue.append(command)
        print(f"Received and queued command: {command}")
        return {'status': 'ok', 'queued': command}, 200
    else:
        return {'status': 'error', 'message': 'No command received'}, 400

@app.route('/command', methods=['GET'])
def get_commands():
    # نرجّع كل الأوامر ثم نفرغ القائمة
    cmds = list(command_queue)
    command_queue.clear()
    print(f"Sending {len(cmds)} command(s) to client")
    return jsonify({'commands': cmds}), 200

@app.route('/', methods=['GET'])
def get_status():
    return jsonify(status='running'), 200

if __name__ == '__main__':
    # تشغيل على كل الواجهات على بورت 5000
    app.run(host='0.0.0.0', port=5000)
