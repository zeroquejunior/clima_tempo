from flask import Flask, render_template
from sqlalchemy import engine
from sqlalchemy.sql.expression import select, table
from app.controller import config
import app


app = Flask(__name__)

@app.route('/')
def index(id=3477, token='b22460a8b91ac5f1d48f5b7029891b53'):
    # id = int(input('Digite o ID da cidade que deseja consultar: '))
    # config.buscar_dados(id)
    return  render_template('home.html')

def busca_db_data(data_i, data_f):
    data_i = str(input('Digite a data inicial dd/mm/ano: ')).strip
    data_f = str(input('Digite a data final dd/mm/ano: ')).strip

    with engine.begin() as connection:
        data_i = connection.execute(table.select('forcast_days_15'))
        connection.execute(table.__getattribute__(), {"date_br"})
        data_f = connection.execute(table.select('forcast_days_15'))
        connection.execute(table.__getattribute__(), {"date_br"})
    return print(f'Data inicial {data_i} e data final {data_f}')

