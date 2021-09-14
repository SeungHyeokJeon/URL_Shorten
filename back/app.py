from flask import Flask, request
from flask_restx import Api, Resource
import urllib.request
import urllib.parse
import json

# secret keys
secrets = json.loads(open('./secrets.json').read())

app = Flask('url_shorten')
api = Api(app)
client_id = secrets['client_id']
client_secret = secrets['client_secret']


@api.route('/url')
class shortUrl(Resource):
    def get(self):
        param = request.args.to_dict()

        if len(param) == 0:
            return 'no url'
        url = param['url']

        enc_text = urllib.parse.quote(url)
        data = 'url=' + enc_text
        request_naver = urllib.request.Request('https://openapi.naver.com/v1/util/shorturl')
        request_naver.add_header('Access-Control-Allow-Origin', '*')
        request_naver.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
        request_naver.add_header('X-Naver-Client-Id', client_id)
        request_naver.add_header('X-Naver-Client-Secret', client_secret)
        response = urllib.request.urlopen(request_naver, data=data.encode('utf-8'))
        rescode = response.getcode()
        if rescode == 200:
            response_body = response.read().decode('utf-8')
            response_body_json = json.loads(response_body)
            return {"url": response_body_json['result']['url']}
        else:
            return {'Error Code': 200}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=12098)