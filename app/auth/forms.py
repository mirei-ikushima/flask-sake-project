from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import InputRequired, EqualTo, Email
from ..models import User


class RegistrationForm(FlaskForm):
    username = StringField("Username:", validators=[InputRequired()])
    email = StringField("Your Email Address:", validators=[InputRequired(), Email()])
    password = PasswordField("Password:", validators=[InputRequired(),
                                                      EqualTo("confirm_password",
                                                              message="Password entries must match")])
    confirm_password = PasswordField("Confirm Password:", validators=[InputRequired()])
    submit = SubmitField("Register")

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError("That email has already been used to create an account")

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError("There is already an account with that username")


class LoginForm(FlaskForm):
    username = StringField("Username:", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    remember_me = BooleanField("Remember me?")
    submit = SubmitField("Sign In")


class PasswordResetRequest(FlaskForm):
    email = StringField('Email Address:', validators=[InputRequired(), Email()])
    submit = SubmitField('Send Request')


class PasswordResetForm(FlaskForm):
    new_password1 = PasswordField('New Password:', validators=[InputRequired()])
    new_password2 = PasswordField('Repeat Password:', validators=[InputRequired(), EqualTo("new_password2")])
    submit = SubmitField("Reset Password")
