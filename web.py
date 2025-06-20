from flask import Flask, request, jsonify
from flask_cors import CORS
from bazi.main import get_bazi_info  # ← baziライブラリの命式関数（既にある場合）

app = Flask(__name__)
CORS(app)

@app.route("/ping")
def ping():
    return jsonify({"message": "pong", "status": "ok"})

@app.route("/shichu", methods=["POST"])
def shichu():
    data = request.json
    birthdate = data.get("birthdate")  # "1990-01-01"
    birthtime = data.get("birthtime")  # "14:30"

    if not birthdate or not birthtime:
        return jsonify({"error": "birthdate and birthtime are required"}), 400

    try:
        result = get_bazi_info(birthdate, birthtime)
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
