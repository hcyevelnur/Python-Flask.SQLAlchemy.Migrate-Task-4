from extensions import db   
from app import *

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    year = db.Column(db.Integer)
    imdb = db.Column(db.Float)
    producer_id = db.Column(db.Integer, db.ForeignKey('producer.id'))
    producer = db.relationship('Producer', backref = db.backref('movies', lazy = True))
    status = db.Column(db.Boolean, default = True)

    def __repr__(self):
        return self.name

    def __init__(self, name, year, imdb, producer_id, status):
        self.name = name
        self.year = year
        self.imdb = imdb
        self.producer_id = producer_id
        self.status = status

    def save(self):
        db.session.add(self)
        db.session.commit()



class Producer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()
    


class ContactUs(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    comment = db.Column(db.String(100))

    def __repr__(self):
        return self.full_name

    def __init__(self, full_name, email, phone, comment):
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.comment = comment

    def save(self):
        db.session.add(self)
        db.session.commit()

class RecMovie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    movie_name = db.Column(db.String(100))
    producer = db.Column(db.String(100))
    year = db.Column(db.Integer)
    your_point = db.Column(db.Integer)

    def __repr__(self):
        return self.movie_name

    def __init__(self, movie_name, producer, year, your_point):
        self.movie_name = movie_name
        self.producer = producer
        self.year = year
        self.your_point = your_point

    def save(self):
        db.session.add(self)
        db.session.commit()