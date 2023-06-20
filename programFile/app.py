from flask import Flask, request, jsonify
from flask_restx import Api, Resource 
import sys
from flask_cors import CORS
import os
sys.path.append(os.getcwd())
from heromatch import *
app = Flask(__name__)
CORS(app)
api = Api(app)  # Flask 객체에 Api 객체 등록
#@app.route('/call-python-function', methods=['POST'])

@api.route('/heromatch/<string:text>')  # url pattern으로 name 설정
class Hello(Resource):
    def get(self, text):  # 멤버 함수의 파라미터로 name 설정
        result, desc = promptV2('ko', text)
        df = getRedditText(result)
        makeWordCloud(df, result)
        bf = find_friend(result)
        if bf == 'False':
            bf = "%ss와 친한 히어로는 없었습니다😥" % result
        else:
            bf = bf   
        return {"name" : "%s" % result, "desc" : "%s" % desc, "bf" : "%s" % bf }
    
#if __name__ == "__main__":
#    app.run(debug=True, host='0.0.0.0', port=80)

if __name__ == '__main__':
    app.run() 