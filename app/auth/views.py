from flask import redirect, url_for, render_template, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_babel import _
from . import auth
from .forms import RegistrationForm, LoginForm, PasswordResetRequest, PasswordResetForm
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

    title = _("Register")
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
            flash(_("Incorrect username or password"))

    title = _("Log in")
    return render_template("auth/login.html",
                           login_form=login_form,
                           title=title)


@auth.route('/request_password_reset', methods=['GET', 'POST'])
def request_reset_password():

    if current_user.is_authenticated:
        return redirect(url_for('main.collection',
                                name=current_user.username))

    request_form = PasswordResetRequest()
    if request_form.validate_on_submit():
        user = User.query.filter_by(email=request_form.email.data).first()

        if user:
            token = user.get_reset_token()
            send_email("Sake Collection - Reset your password", "email/password_reset_mail",
                       user.email, user=user, token=token)
        return redirect(url_for('auth.login'))

    return render_template("auth/reset_pass_request.html",
                           request_form=request_form,
                           title=_("Request Password Reset"))


@auth.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.collection',
                                name=current_user.username))

    user = User.verify_reset_token(token)

    if not user:
        return redirect(url_for('main.index'))

    reset_form = PasswordResetForm()
    if reset_form.validate_on_submit():
        user.password = reset_form.new_password1.data
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('auth/reset_password.html',
                           title=_('Reset Password'),
                           reset_form=reset_form)


@auth.route('/logout')
@login_required
def log_out():
    logout_user()
    return redirect(url_for("main.index"))
