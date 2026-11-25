
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "application": "DevSecOps Flask Application",
        "status": "running",
        "message": "Welcome Engineer!"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

@app.route("/api/users")
def users():
    return jsonify({
        "users": [
            {"id": 1, "name": "Engineer 1"},
            {"id": 2, "name": "Engineer 2"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
