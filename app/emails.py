from flask import render_template
from flask_mail import Message
from . import mail
import os


def send_email(subject, template, recipients, **kwargs):
    sender = os.environ.get("MAIL_USERNAME")

    msg = Message(subject, sender=sender, recipients=[recipients])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)
