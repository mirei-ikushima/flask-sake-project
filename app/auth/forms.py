from flask_wtf import FlaskForm
from flask_babel import _
from flask_babel import lazy_gettext as _l
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import InputRequired, EqualTo, Email
from ..models import User


class RegistrationForm(FlaskForm):
    username = StringField(_l("Username:"), validators=[InputRequired()])
    email = StringField(_l("Your Email Address:"), validators=[InputRequired(), Email()])
    password = PasswordField(_l("Password:"), validators=[InputRequired(),
                                                          EqualTo("confirm_password",
                                                          message=_("Password entries must match"))])
    confirm_password = PasswordField(_l("Confirm Password:"), validators=[InputRequired()])
    submit = SubmitField(_l("Register"))

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError(_("That email has already been used to create an account"))

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError(_("There is already an account with that username"))


class LoginForm(FlaskForm):
    username = StringField(_l("Username:"), validators=[InputRequired()])
    password = PasswordField(_l("Password:"), validators=[InputRequired()])
    remember_me = BooleanField(_l("Remember me?"))
    submit = SubmitField(_l("Sign In"))


class PasswordResetRequest(FlaskForm):
    email = StringField(_l('Email Address:'), validators=[InputRequired(), Email()])
    submit = SubmitField(_l('Send Request'))


class PasswordResetForm(FlaskForm):
    new_password1 = PasswordField(_l('New Password:'), validators=[InputRequired()])
    new_password2 = PasswordField(_l('Repeat Password:'), validators=[InputRequired(), EqualTo("new_password2")])
    submit = SubmitField(_l("Reset Password"))
