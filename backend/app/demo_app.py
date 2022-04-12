from flask import Flask, request, jsonify, current_app, g
import json
import sqlite3
from flask_cors import CORS
from pathlib import Path
import argparse

DATABASE = "app/db/demo_app.db"

def clean_start():
    # reset the database
    init_db()
    

def allowed_file(filename):
    """
    Check if the file is allowed
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def make_dicts(cursor, row):
    """
    Convert the sqlite3 cursor to a list of dictionaries
    """
    return dict((cursor.description[idx][0], value) for idx, value in enumerate(row))


def get_db():
    """
    connect to the sqlite db
    """
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = make_dicts
    return db


def init_db():
    """
    Initialize the database
    """
    with app.app_context():
        db = get_db()
        with current_app.open_resource("db/schema.sql", mode="r") as f:
            db.cursor().executescript(f.read())
        db.commit()


def write_db(query, args=()):
    """
    Write to the database
    """
    db = get_db()
    db.execute(query, args)
    db.commit()


def write_db_ret_last(query, args=()):
    """
    Write to the database, returning the last inserted id
    """
    db = get_db()
    db.execute(query, args)
    db.commit()
    id = db.execute("SELECT last_insert_rowid()").fetchone()["last_insert_rowid()"]
    return id


def query_db(query, args=(), one=False):
    """
    Query the database
    """
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
# uncomment this line to reset the db on app start
# clean_start()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    return jsonify({"message": "Hit backend root endpoint!"})


@app.route("/exampleGetEndpoint", methods=["GET"])
def exampleGetEndPoint():
    """
    example get endpoint
    """
    return jsonify({"message":"Hello from the server!"})

@app.route("/examplePostEndpoint", methods=["POST"])
def examplePostEndpoint():
    """
    example post endpoint
    """
    data = request.get_json()
    # check if the request has a pt_id
    if "name" in data:
        name = data["name"]
    else:
        return jsonify({"error":"No name key in json object I received"})
    if "description" in data:
        description = data["description"]
    else:
        return jsonify({"error":"No description key in json object I received"})
    return jsonify({"message": "received message with name and description", "name":name, "description":description})

# we can use the sqlite database for some sort of persistence if we want, leaving out an example for that for now

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
