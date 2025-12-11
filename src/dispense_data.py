import json
from datetime import datetime, time
import math

def load_data():
    readings = []
    with open("weight_data.json", "r") as f:
        for line in f:
            try:
                d = json.loads(line)

                # Convert timestamp (string → float → datetime)
                ts = float(d["timestamp"])

                # Convert weight (string → float)
                wt = float(d["weight"])

                readings.append({
                    "timestamp": ts,
                    "weight": wt
                })
            except Exception as e:
                print("Skipped bad line:", e)
    return readings

def average_time_of_day(timestamps):
    # Convert each timestamp into a time-of-day angle on the unit circle
    angles = []
    for dt in timestamps:
        seconds = dt.hour * 3600 + dt.minute * 60 + dt.second
        angle = (seconds / 86400) * 2 * math.pi
        angles.append(angle)

    # Compute average vector
    x = sum(math.cos(a) for a in angles) / len(angles)
    y = sum(math.sin(a) for a in angles) / len(angles)

    # Convert back to angle
    avg_angle = math.atan2(y, x)
    if avg_angle < 0:
        avg_angle += 2 * math.pi

    # Convert angle → seconds → time of day
    avg_seconds = avg_angle / (2 * math.pi) * 86400
    avg_seconds = int(avg_seconds)

    hour = avg_seconds // 3600
    minute = (avg_seconds % 3600) // 60
    second = avg_seconds % 60

    return time(hour, minute, second)

def show_analytics():
    data = load_data()

    if not data:
        print("No data recorded.")
        return

    weights = [d["weight"] for d in data]
    times = [datetime.fromtimestamp(d["timestamp"]) for d in data]

    print("\n--- Analytics ---")
    print(f"Total readings: {len(weights)}")
    print(f"Highest weight: {max(weights)} g")
    print(f"Lowest weight:  {min(weights)} g")
    print(f"Average weight: {sum(weights)/len(weights):.2f} g")

    print("\nFirst reading:", times[0], "->", weights[0], "g")
    print("Last reading: ", times[-1], "->", weights[-1], "g")
    avg_time = average_time_of_day(times)
    print(f"Average time of day for readings: {avg_time}")

    # Simple trend check
    if weights[-1] < weights[0]:
        print("\nTrend: Food level has decreased over time.")
    elif weights[-1] > weights[0]:
        print("\nTrend: Food level has increased over time.")
    else:
        print("\nTrend: No change in overall weight.")

if __name__ == "__main__":
    show_analytics()

        