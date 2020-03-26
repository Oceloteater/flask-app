from flask_restful import Resource, reqparse
from models.dog import DogModel


class Dog(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Doggo needs a name')
    parser.add_argument('breed', type=str, required=True, help='Doggo needs a breed')

    def get(self, name):
        dog = DogModel.get_by_name(name)
        if dog:
            return dog.json()

        return {'message': 'Doggo not found'}, 404

    def post(self, name):
        pass

    def put(self, name):
        pass

    def delete(self, name):
        pass


class DogList(Resource):
    def get(self):
        return {'dogs': [dog.json() for dog in DogModel.query.all()]}
