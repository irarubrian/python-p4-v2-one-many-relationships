from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Ensure Flask-Migrate is initialized

# Import models after initializing db
from models import Employee, Worker  # Ensure this matches your models

if __name__ == "__main__":
    app.run(debug=True)
