from flask import Flask, jsonify
from flask_cors import CORS
import psutil
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

    cpu = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory().percent

    disk = psutil.disk_usage('/').percent

    data = {
        "status": "Running",
        "containers": "3 Active",
        "cpu": f"{cpu}%",
        "ram": f"{ram}%",
        "disk": f"{disk}%",
        "database": "Connected"
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)