from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators= [DataRequired()])
    email = EmailField("Email address", validators= [DataRequired(), Email()])
    password = PasswordField("Password", validators= [DataRequired()])
    password2 = PasswordField("Repeat Password", validators= [DataRequired(), EqualTo(password)])
    submit = SubmitField("Register")

class SigninForm(FlaskForm):
    username = StringField("Username", validators= [DataRequired()])
    password = PasswordField("Password", validators= [DataRequired()])
    submit = SubmitField("Sign In")

class LogoutForm(FlaskForm):
    submit = SubmitField("Logout")

class VisitForm(FlaskForm):
    place = StringField("Place you want to visit", validators=[DataRequired()])
    rating= StringField("How important is it you go there? 0-5", validators=[DataRequired()])
    submit = SubmitField("Submit")

class ReviewForm(FlaskForm):
    id_num = IntegerField("Id number of the place you wish to review: ", validators=[DataRequired()])
    review = StringField("Quick review in less than 200 characters", validators=[DataRequired()])
    submit = SubmitField("Submit review")