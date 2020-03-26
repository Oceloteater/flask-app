from flask_restful import Resource, reqparse
from models.dog import DogModel


class Dog(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Dog needs a name')
    parser.add_argument('breed', type=str, required=True, help='Dog needs a breed')

    def get(self, name):
        pass

    def post(self, name):
        pass

    def put(self, name):
        pass

    def delete(self, name):
        pass


class DogList(Resource):
    def get(self):
        pass
