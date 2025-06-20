from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ 四柱推命APIへようこそ！"

@app.route("/ping")
def ping():
    return jsonify({"message": "pong", "status": "ok"})
