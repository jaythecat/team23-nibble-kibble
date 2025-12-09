import json
from datetime import datetime
import matplotlib.pyplot as plt

def display_data():
    readings = []

    with open('weight_data.json', 'r') as f:
        for line in f:
            readings.append(json.loads(line))
    times = [datetime.fromtimestamp(r['timestamp']) for r in readings]
    weights = [r['weights'] for r in readings]

    plt.plot(times, weights, marker='o')
    plt.title("Food dispensed over time")
    plt.xlabel("Time")
    plt.ylabel("Weight (grams)")
    plt.grid(True)
    plt.show()

display_data()

        