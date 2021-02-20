from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Email
from ..models import User


class RegistrationForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()])
    email = StringField("Your Email Address:", validators=[DataRequired(), Email()])
    password = PasswordField("Password:", validators=[DataRequired(),
                                                      EqualTo("confirm_password",
                                                              message="Password entries must match")])
    confirm_password = PasswordField("Confirm Password:", validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError("That email has already been used to create an account")

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError("There is already an account with that username")


class LoginForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])
    remember_me = BooleanField("Remember me?")
    submit = SubmitField("Sign In")
