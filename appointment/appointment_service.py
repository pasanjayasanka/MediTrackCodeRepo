from flask import Flask, request, jsonify

app = Flask(__name__)
appointments = []

@app.route('/appointments', methods=['POST'])
def add_appointment():
    appointment = request.json
    appointments.append(appointment)
    return jsonify({"message": "appointment added", "appointments": appointments}), 201

@app.route('/appointments', methods=['GET'])
def get_appointments():
    return jsonify({"appointments": appointments})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
