from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, String, Integer


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)

class ForcastDays15(db.Model):
    __tablename__ = 'forcast_days_15'
    id = db.Column(db.Integer, primary_key=True)
    climatempo_id = db.Column(db.Integer)
    name = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)
    date_br = db.Column(db.DateTime)
    probability = db.Column(db.Integer)
    precipitation = db.Column(db.Integer)
    min = db.Column(db.Integer)
    max = db.Column(db.Integer)
    
    
    def __init__(self, climatempo_id, name, state, country, date_br, probability, precipitation, min, max):
        self.climatempo_id = climatempo_id
        self.name = name
        self.state = state
        self.country = country
        self.date_br = date_br
        self.probability = probability
        self.precipitation = precipitation
        self.min = min
        self.max = max



    def __repr__(self):
        return '<forcast_days_15 %r>' % self.name



db.create_all()




