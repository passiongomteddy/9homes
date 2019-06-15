from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient

## DB 연결
client = MongoClient('localhost', 27017)
db = client.diyproject

## 설명서를 주는 부분 = HTML
@app.route('/')
def main():
   return render_template('main.html')

@app.route('/request')
def req(): ## 함수 정의를 request로 했다가 오류 났었음 (아래의 request.form 과 충돌남, 왜?)
   return render_template('request.html')

@app.route('/result')
def result():
   return render_template('result.html')

@app.route('/post', methods=['POST'])
def save():
    city = request.form['city_give']
    gu = request.form['gu_give']
    dong = request.form['dong_give']

    db.request.insert_one({'city':city,'gu':gu,'dong':dong})

    return jsonify({'result':'success'})

@app.route('/post', methods=['GET'])
def read():
    request_return = list(db.request.find({},{'_id':False}))
    return jsonify({'result':'success', 'req':request_return})


@app.route('/dummy', methods=['POST'])
def dummy():
    return render_template('dummy.html')


if __name__ == '__main__': ## 이 명령어는 맨 뒤에 와야 함!!
   app.run(debug=True)