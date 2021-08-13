from flask import Flask
from views import weather_api
from db import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///storage.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.register_blueprint(weather_api)
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create database tables for our data models

        return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
