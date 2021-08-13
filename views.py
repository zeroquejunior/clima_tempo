from flask import Blueprint
from models import Weather
from services.climatempo_service import ClimatempoService
from utils.parser import climatempo_to_weather
from db import db

weather_api = Blueprint("weather_api", __name__)


@weather_api.route("/api/<id>")
def get_weather(id):
    weather = None

    weather = Weather.query.get(id)
    if weather:
        print(weather)
        return json_parse(weather)

    climatempo = ClimatempoService()
    climatempo_response = climatempo.get(id)
    weather = climatempo_to_weather(climatempo_response)

    db.session.add(weather)

    # return weather.forecasts[0].date
    db.session.commit()

    return json_parse(weather)


def json_parse(weather):
    return {
        "city": weather.city,
        "country": weather.country,
        "state": weather.state,
        "id": weather.id,
        "forecasts": [
            {
                "date": forecast.date,
                "precipitation": forecast.precipitation,
                "probability": forecast.probability,
                "min_temperature": forecast.min,
                "max_temperature": forecast.max,
            }
            for forecast in weather.forecasts
        ],
    }
