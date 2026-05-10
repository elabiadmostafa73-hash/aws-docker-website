from flask import Flask, jsonify
from flask_cors import CORS
import random
import psycopg2

app = Flask(__name__)

CORS(app)

connection = psycopg2.connect(
    host="172.17.0.1",
    database="simnet",
    user="admin",
    password="password"
)

@app.route("/api/stats")
def stats():

    data = {
        "status": "Running",
        "containers": "3 Active",
        "cpu": f"{random.randint(20,70)}%",
        "ram": f"{random.randint(30,80)}%",
        "database": "Connected"
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)