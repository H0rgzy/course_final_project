from app import app, db
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, login_user, current_user
from forms import RegistrationForm, SigninForm
from models import User, Visit


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registration", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    if request.method == "POST":
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
            login_user(user)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("account", _external= True, _scheme="https"))
    return render_template("signin.html", form=form)



# @app.route("/account/<user>")
# @login_required
# def account(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     return render_template("account.html", user=user)

