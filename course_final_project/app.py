from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mydb.db'

app.config["SECRET_KEY"] = "S3cret14"

login = LoginManager(app)
login.login_view ='login'





import routes, models