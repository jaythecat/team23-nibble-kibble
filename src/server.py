from flask import flask
from flask import request

app = Flask(__name__)

@app.route("/")
def getWeight():
    weight = request.args.get("weight")
    time = request.args.get("time")
    print(time)
    print(weight)
    return "We recieved the values: "+ str(time) + " " + str(weight)

