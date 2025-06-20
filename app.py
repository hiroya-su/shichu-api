from flask import Flask, request, jsonify
from flask_cors import CORS
from bazi import analyze_bazi  # あなたのAPI処理関数（例）

app = Flask(__name__)
CORS(app)

@app.route("/ping")
def ping():
    return jsonify({"message": "pong", "status": "ok"})

@app.route("/shichu")
def shichu():
    # 例: クエリパラメータから情報取得
    name = request.args.get("name", "名無し")
    year = int(request.args.get("year", 2000))
    month = int(request.args.get("month", 1))
    day = int(request.args.get("day", 1))
    hour = int(request.args.get("hour", 12))
    city = request.args.get("city", "Tokyo")

    # 四柱推命ロジックの呼び出し
    result = analyze_bazi(year, month, day, hour, city)

    return jsonify({
        "name": name,
        "bazi": result
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)