from flask import Flask, jsonify
from flask_cors import CORS

import random

app = Flask(__name__)
CORS(app)
# Function to generate random sensor values
def generate_sensor_data():
    return {
        "carbon": random.randint(0, 100),
        "nitrogen": random.randint(0, 100),
        "co2": random.randint(0, 100),
        "methane": random.randint(0, 100),
        "moisture": random.randint(0, 100),
    }

# Define the `/api/sensors` endpoint
@app.route('/api/sensors', methods=['GET'])
def get_sensor_data():
    return jsonify(generate_sensor_data())



if __name__ == '__main__':
    app.run(debug=True)
