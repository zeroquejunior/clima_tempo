from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from db import db


class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)
    forecasts = relationship("DailyForecast")


class DailyForecast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weather_id = db.Column(db.Integer, ForeignKey("weather.id"))
    date = db.Column(db.String())
    probability = db.Column(db.Integer)
    precipitation = db.Column(db.Integer)
    min = db.Column(db.Integer)
    max = db.Column(db.Integer)
