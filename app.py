from flask import Flask, request, jsonify
from flask_cors import CORS
from bazi import Bazi

app = Flask(__name__)
CORS(app)

@app.route('/sichu', methods=['POST'])
def sichu():
    data = request.get_json()
    name = data.get('name')
    birth = data.get('birthdate')  # 'YYYY-MM-DD'
    time = data.get('birthtime')   # 'HH:MM'
    gender = data.get('gender')

    year, month, day = birth.split('-')
    hour = time.split(':')[0]

    b = Bazi(int(year), int(month), int(day), int(hour))
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
