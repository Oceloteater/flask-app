from db import db


class DogModel(db.Model):
    __tablename__ = 'dogs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    breed = db.Column(db.String(80))
    age = db.Column(db.Integer)

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def json(self):
        return {'name': self.name, 'breed': self.breed, 'age': self.age}

    @classmethod
    def get_from_db(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
