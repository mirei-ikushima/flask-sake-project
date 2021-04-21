from app import create_app
from flask import render_template
from flask_mail import Message
from . import mail
from threading import Thread
import os


def async_email(create_app, msg):
    with create_app().app_context():
        mail.send(msg)


def send_email(subject, template, recipients, **kwargs):
    sender = os.environ.get("MAIL_USERNAME")

    msg = Message(subject, sender=sender, recipients=[recipients])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    Thread(target=async_email, args=(create_app, msg)).start()
