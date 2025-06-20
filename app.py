# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from bazi import BaZi

app = Flask(__name__)
CORS(app)

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong", "status": "ok"})

@app.route("/shichu", methods=["POST"])
def shichu():
    try:
        data = request.json
        year = int(data.get("year"))
        month = int(data.get("month"))
        day = int(data.get("day"))
        time = int(data.get("time"))

        bazi = BaZi(year, month, day, time)
        result = bazi.fourpillars()

        return jsonify({
            "status": "ok",
            "data": result
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
