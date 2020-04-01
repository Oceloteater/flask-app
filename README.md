# flask-app

Notes on implementation, requirements and running the app

## Technologies

This application uses the following technologies:
- [Python3.8](https://www.python.org/downloads/release/python-380/) version
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) REST framework
- [SQLAlchemy](https://www.sqlalchemy.org/) and [SQLite3](https://www.sqlite.org/index.html) for db solution
- [Redis](https://redis.io/) for caching

Rationale for using these technologies are that Flask-RESTful is the standard and a requirement of the task. SQLAlchemy allows you to swap out db implementations easily. SQLite is simple db solution but better than using in-memory store. And Redis is the latest caching option of choice for modern apps. 

Basic structure was inspired from here:

    https://www.udemy.com/course/rest-api-flask-and-python/
    
## Requirements

- [Python](https://www.python.org/downloads/release/python-380/) 3.8
- [Redis](https://redis.io/) 5.8

## Running

Installing dependencies:
```shell
pip install -r requirements.txt
```
Run redis server:
```shell
[__dir__]/Redis/redis-server.exe

'localhost', 6379
```
Run app:
```shell
[__dir__]/git-projects/flask-app

python app.py

(creates data.db) in your root directory
```
URI:

    http://127.0.0.1:5000/
Resources
    
    (Dog, '/dog/<string:name>')
    (DogList, '/dogs')
    
## Notes

### Task 1: (Create a Dog Application)
Implemented:
- Create - new dog with id, name, breed and age
- Read - return list of dogs and get individual dog by name (not id)
- Update - existing dog or create new one if not found
- Delete - remove a given individual dog
- Datastore - SQLite db


### Task 2: (Implement Validation)
Implemented:
- Simple validation using reqparse


### Task 3: (Implement Caching)
Implemented:
- Simple caching using Redis


### Task 4: (Implement Configuration)
Not Implemented:
- No (bonus) config
- No unit tests
