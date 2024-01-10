from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/python/hello')
def hello():
    response = {}
    response['message'] = 'hello world'
    return response