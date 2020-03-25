from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return 'Hello world'


app.run(port=5000)
