from models import Weather, DailyForecast
import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from db import db


def climatempo_to_weather(climatempo_response):
    weather = Weather()
    weather.id = climatempo_response["id"]
    weather.city = climatempo_response["name"]
    weather.state = climatempo_response["state"]
    weather.country = climatempo_response["country"]
    weather.forecasts = climatempo_data_to_daily_forecasts(climatempo_response["data"])

    return weather


def climatempo_data_to_daily_forecasts(data):
    forecasts = []
    for item in data:
        rain = item["rain"]
        temperature = item["temperature"]

        daily_forecast = DailyForecast()

        daily_forecast.date = item["date"]
        daily_forecast.probability = rain["probability"]
        daily_forecast.precipitation = rain["precipitation"]
        daily_forecast.max = temperature["max"]
        daily_forecast.min = temperature["min"]

        forecasts.append(daily_forecast)

    return forecasts
