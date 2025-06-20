from flask import Flask, request, jsonify
from flask_cors import CORS
from bazi import Bazi
import os
if os.environ.get("RENDER") == "true":
    exit()  # Render環境では無視

app = Flask(__name__)
CORS(app)

@app.route('/sichu', methods=['POST'])
def sichu():
    try:
        data = request.get_json()
        name = data.get('name')
        birth = data.get('birthdate')  # 'YYYY-MM-DD'
        time = data.get('birthtime')   # 'HH:MM'
        gender = data.get('gender')

        year, month, day = map(int, birth.split('-'))
        hour = int(time.split(':')[0])

        b = Bazi(year, month, day, hour)

        pillars = [{
            "干": p.stem,
            "支": p.branch,
            "通変星": p.get_tongbianxing(),
            "蔵干": p.get_zanggan(),
            "五行": p.get_wuxing(),
        } for p in b.pillars]

        return jsonify({
            "name": name,
            "gender": gender,
            "命式": pillars,
            "comment": ""
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
