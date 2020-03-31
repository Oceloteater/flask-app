from flask_restful import Resource, reqparse
from models.dog import DogModel
import json
import redis

redis = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)


class Dog(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('breed', type=str, required=True, help='Doggo needs a breed')
    parser.add_argument('age', type=int, required=True, help='Doggo needs an age')

    """
    GET /dog
    """
    def get(self, name):
        dog = redis.get(name)
        if dog:
            print('-- This is coming from cache --')
            return json.loads(dog)
        else:
            dog = DogModel.get_from_db(name)
            if dog:
                redis.setex(dog.name, 90, json.dumps(dog.json()))
                return dog.json()

            return {'message': 'Doggo not found'}, 404

    """
    POST /dog
    """
    def post(self, name):
        if DogModel.get_from_db(name):
            return {'message': '{} already exists'.format(name)}, 400

        data = Dog.parser.parse_args()
        dog = DogModel(name, data['breed'], data['age'])

        try:
            dog.save_to_db()
        except:
            return {'message': 'An error occurred saving doggo'}, 500

        return dog.json(), 201

    """
    PUT /dog
    """
    def put(self, name):
        data = Dog.parser.parse_args()
        dog = DogModel.get_from_db(name)

        if dog is None:
            dog = DogModel(name, data['breed'], data['age'])
        else:
            dog.breed = data['breed']
            dog.age = data['age']

        try:
            dog.save_to_db()
        except:
            return {'message': 'An error occurred saving doggo'}, 500

        return dog.json(), 200

    """
    DELETE /dog
    """
    def delete(self, name):
        item = DogModel.get_from_db(name)

        if item:
            item.delete_from_db()
            return {'message': 'Doggo put down'}
        else:
            return {'message': 'Doggo does not exist'}


class DogList(Resource):

    """
    GET /dogs
    """
    def get(self):
        return {'dogs': [dog.json() for dog in DogModel.query.all()]}
