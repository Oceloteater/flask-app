from flask_restful import Resource, reqparse
from models.dog import DogModel


class Dog(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('breed', type=str, required=True, help='Doggo needs a breed')

    def get(self, name):
        dog = DogModel.get_by_name(name)
        if dog:
            return dog.json()

        return {'message': 'Doggo not found'}, 404

    def post(self, name):
        if DogModel.get_by_name(name):
            return {'message': '"{}" already exists'.format(name)}, 400

        data = Dog.parser.parse_args()
        dog = DogModel(name, data['breed'])

        try:
            dog.save_to_db()
        except:
            return {'message': 'An error occurred saving doggo'}, 500

        return dog.json(), 201

    def put(self, name):
        pass

    def delete(self, name):
        pass


class DogList(Resource):
    def get(self):
        return {'dogs': [dog.json() for dog in DogModel.query.all()]}
