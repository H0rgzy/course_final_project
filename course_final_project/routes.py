from app import app, db, login
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, login_user, current_user, logout_user
from forms import LogoutForm, RegistrationForm, SigninForm, VisitForm
from models import User, Visit
from werkzeug.urls import url_parse


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registration", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.password.data == form.password2.data:
            user = User(username = form.username.data, email = form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash(' You are now registered')
            return redirect(url_for("signin"))
        else:
            flash("Passwords do not match")
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

            return redirect(next or url_for("signin"))
        
    return render_template("signin.html", form=form)



@login.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('signin'))


@app.route("/account", methods=["POST", "GET"])
@login_required
def account():
    form = LogoutForm()
    user = current_user
    user = User.query.filter_by(username=user.username).first()
    if request.method == "POST":
        logout()
    return render_template("account.html",user=user, form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("signin"))

@app.route("/visit", methods=["POST", "GET"])
@login_required
def visit():
    form = VisitForm()
    user = current_user
    user = User.query.filter_by(username = user.username).first()
    
    places = Visit.query.all()
    
    if request.method == "POST":
        place = Visit(place=form.place.data, user_id=user.id, rating=form.rating.data)
        db.session.add(place)
        db.session.commit()
        flash("The place has been successfully added")
        return render_template("visit.html", form=form, user=user, places=places)
    return render_template("visit.html", form=form, user=user, places=places)

@app.route("/visit/delete/<int:place_id>", methods=["POST"])
@login_required
def delete_place(place_id):
    place = Visit.query.get_or_404(place_id)
    db.session.delete(place)
    db.session.commit()
    flash("Place deleted")
    return redirect(url_for("visit", _external=True, _scheme="http"))

