from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mydb.db'

app.config["SECRET_KEY"] = "S3cret14"

login_manager = LoginManager()
login_manager.init_app(app)


import models, routes