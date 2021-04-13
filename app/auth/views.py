from flask import redirect, url_for, render_template, flash
from flask_login import login_user, logout_user, login_required
from . import auth
from .forms import RegistrationForm, LoginForm
from ..models import User
from ..emails import send_email
from .. import db


@auth.route('/register', methods=['GET', 'POST'])
def register():
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        user = User(username=reg_form.username.data, password=reg_form.password.data,
                    email=reg_form.email.data)
        db.session.add(user)
        db.session.commit()

        send_email("Welcome to Sake Collection!", "email/welcome_msg",
                   user.email, user=user)
        return redirect(url_for("auth.login"))

    title = "Register"
    return render_template("auth/register.html",
                           reg_form=reg_form,
                           title=title)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember_me.data)
            return redirect(url_for("main.collection",
                                    name=user.username))
        else:
            flash("Incorrect username or password")

    title = "Log in"
    return render_template("auth/login.html",
                           login_form=login_form,
                           title=title)


@auth.route('/logout')
@login_required
def log_out():
    logout_user()
    return redirect(url_for("main.index"))
