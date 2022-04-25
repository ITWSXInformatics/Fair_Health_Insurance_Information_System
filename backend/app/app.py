from flask import Flask, request, jsonify, current_app, g, session
import json
import sqlite3
from flask_cors import CORS
from pathlib import Path
import argparse

# change for production for security
income = None
age = None
dependents = None
gender = None

ref_income = {
    '<$40,000' : 10000,
    '$40,000-$60,000' : 15000,
    '$60,001-80,001' : 20000,
    '$80,001-$100,000' : 25000,
    '>$100,000' :30000
}

ref_age_sex  = {
    '<21' : {
    'male' : 4000,
    'female' : 3500
    },
    '21-39' : {
    'male' : 6000,
    'female' : 7500
    },
    '40-59' : {
    'male' : 6250,
    'female' : 8000
    },
    '60-79' : {
    'male' : 18000,
    'female' : 20000
    },
    '80+' : {
    'male' : 20000,
    'female' : 22000
    }
}

ref_dependents = {
    '0' : 1.0,
    '1' : 1.2,
    '2' : 1.6,
    '3-4' : 2.5,
    '4+' : 4
}

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def index():
    return jsonify({"message": "Hit backend root endpoint!"})

# @app.route("/exampleGetEndpoint", methods=["GET"])
# def exampleGetEndPoint():
#     """
#     example get endpoint
#     """
#     return jsonify({"message":"Hello from the server!"})

@app.route("/survey", methods=["POST"])
def survey():
    """
    takes user answers to survey
    """
    data = request.get_json()
    # check if the request has a pt_id

    for(k in ["income", "age", "dependents", "gender"]):
        if k in data:
            vars[k] = data[k]
        else:
            return jsonify({"error": "No {} key in recieved json object".format(k)})

    return jsonify({"message": "survey inputs received"})

@app.route("/results", methods=["POST"])
def results():
    data = request.get_json()
    if "value" in data:
        value = data['value']
    else:
        return jsonify({"error": "No value key in recieved json object"})

    r = ref_age_sex[age][gender] * ref_dependents[dependents]
    m = ref_income[income]

    if value > r:
        r += value * (1 + value / m)

    r = m if r > m else r

    return jsonify({"baseline" : "r"})

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host", type=str, default="0.0.0.0", help="Host address of the app"
    )
    parser.add_argument(
        "--production", action="store_true", help="Run in production mode (debug off)."
    )
    args = parser.parse_args()

    debug = not args.production
    app.run(host="0.0.0.0", debug=debug)
