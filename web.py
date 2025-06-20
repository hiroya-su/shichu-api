from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ 四柱推命APIへようこそ！"

@app.route("/ping")
def ping():
    return jsonify({"message": "pong", "status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Renderが設定するPORTを取得
    app.run(host="0.0.0.0", port=port)

