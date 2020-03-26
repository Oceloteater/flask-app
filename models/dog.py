from db import db


class DogModel(db.Model):
    __tablename__ = 'dogs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    breed = db.Column(db.String(80))

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def json(self):
        return {'name': self.name, 'breed': self.breed}

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()