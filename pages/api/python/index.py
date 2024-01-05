from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/python/hello')
def transformShortLink():
    response = {}
    response['message'] = 'hello world'
    return response

#if __name__ == '__main__':
    #app.run(host = '127.0.0.1', port = 8000)