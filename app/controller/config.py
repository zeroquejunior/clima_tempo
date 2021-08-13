import requests
import json
from pandas.io.json import json_normalize
import pandas
from sqlalchemy import create_engine, engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Integer, String
from flask import Flask


def buscar_dados(id, token):
    
    request = requests.get(f'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{id}/days/15?token={token}')
    response = request.json()
    info = pandas.json_normalize(response, 'data', ['id', 'name', 'state', 'country'])

    return info

data = buscar_dados(3478, 'b22460a8b91ac5f1d48f5b7029891b53')
data = data[['id', 'name', 'state', 'country', 'date_br', 'rain.probability', 'rain.precipitation', 'temperature.min', 'temperature.max']]

engine = create_engine('sqlite:///storage.db', echo=False)
data.to_sql('forcast_days_15', con=engine, if_exists='append', index=True, dtype={'id': Integer(), 'name':String() , 'state': String(), 'country': String(), 'date_br': String(), 'rain.probability': Integer(), 'rain.precipitation': Integer(), 'temperature.min': Integer(), 'temperature.max': Integer()})
engine.execute("SELECT * FROM forcast_days_15").fetchall()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)

