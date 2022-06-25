from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, EqualTo, Email


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators= [DataRequired()])
    email = EmailField("Email address", validators= [DataRequired(), Email()])
    password = PasswordField("Password", validators= [DataRequired()])
    password2 = PasswordField("Repeat Password", validators= [DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

class SigninForm(FlaskForm):
    username = StringField("Username", validators= [DataRequired()])
    password = PasswordField("Password", validators= [DataRequired()])
    submit = SubmitField("Sign In")

class LogoutForm(FlaskForm):
    submit = SubmitField("Logout")