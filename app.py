from flask import Flask, request, jsonify
from flask_cors import CORS
from bazi.main import EightChar

app = Flask(__name__)
CORS(app)

@app.route("/ping")
def ping():
    return jsonify({"message": "pong", "status": "ok"})

@app.route("/shichu", methods=["POST"])
def get_shichu():
    data = request.get_json()
    try:
        year = int(data["year"])
        month = int(data["month"])
        day = int(data["day"])
        time = int(data["time"])

        ec = EightChar(year, month, day, time)
        result = {
            "年柱": ec.get_year_gz(),
            "月柱": ec.get_month_gz(),
            "日柱": ec.get_day_gz(),
            "時柱": ec.get_hour_gz()
        }

        return jsonify({"status": "ok", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
