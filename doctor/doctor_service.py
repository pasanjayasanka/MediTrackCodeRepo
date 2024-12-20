from flask import Flask, request, jsonify

app = Flask(__name__)
doctors = []

@app.route('/doctors', methods=['POST'])
def add_doctor():
    pdoctor = request.json
    doctors.append(doctor)
    return jsonify({"message": "doctor added", "doctors": doctors}), 201

@app.route('/doctors', methods=['GET'])
def get_doctors():
    return jsonify({"doctors": doctors})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
