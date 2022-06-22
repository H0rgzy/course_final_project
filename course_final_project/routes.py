from app import app, db
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, login_user, current_user
from forms import RegistrationForm, SigninForm
from models import User, Visit
from werkzeug.urls import url_parse


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registration", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    if request.method == 'POST':
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(' You are now registered')
        return redirect(url_for("signin"))
    return render_template("registration.html", form=form)
    

@app.route("/signin", methods= ["POST", "GET"])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and user.check_password(form.password.data):
            print('success')
            login_user(user)
            
            next = request.args.get('next')
            if not next or url_parse(next).netloc != '':
                next = url_for('account')
                return redirect(next)

            return redirect(next or url_for("account"))
        
    return render_template("signin.html", form=form)



@app.route("/account")
@login_required
def account():
    return "you are logged in"

