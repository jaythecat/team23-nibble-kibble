from flask import flask
from flask import request
from datetime import datetime
import json


def save_reading(time, weight)
    """Append new reading to file"""
    reading = {
        "timestamp": time,
        "weight": weight
    }

    with open('weight_data.json', 'a') as f:
        f.write(json.dumps(reading) + '\n')

def read_weight_data():
    """Reads all the saved weight data"""
    readings = []

    with open('weight_data.json', 'r') as f:
        for line in f:
            readings.append(json.loads(line))
    for reading in readings:
        dt = datetime.fromtimestamp(reading['timestamp'])
        print(f"{dt}: {reading['weight']}g")

app = Flask(__name__)

@app.route("/")
def getWeight():
    weight = request.args.get("weight")
    time = request.args.get("time")
    if time is None or weight is None:
        return "Incomplete data"
    
    print(f"Time: {dt}")
    print(f"Weight: {weight}")
    save_reading(dt, weight)

    return "We recieved the values: "+ str(time) + " " + str(weight)

