from flask import Flask, Blueprint, url_for, render_template, redirect, request
from flask import current_app as app
from .forms import *
from flask_mail import Mail, Message
import os

mail = Mail()

# Declare Blueprint
main = Blueprint(name='main',
                import_name=__name__, 
                static_folder='main/static',
                static_url_path=None, 
                template_folder='templates',
                url_prefix=None,
                subdomain=None, 
                url_defaults=None, 
                root_path=None)

@main.route('/', methods=['GET', 'POST'])
def index():

    contact = ContactForm()
    if contact.validate_on_submit():
        
        # Get form data
        name = contact.name.data
        email = contact.email.data
        message = contact.message.data

        msg = Message(subject=f"Contact Request <{name}>",
                      sender="femiafreelance@gmail.com",
                      recipients=["femiafreelance@gmail.com"],
                      body=f"Sender Name: {name}\nSend Email: {email}\n\nBEGIN MESSAGE--------------\n\n{message}\n\nEND MESSAGE--------------")
        mail.send(msg)

        return redirect(url_for('main.index'))

    return render_template(
        'index.html',
        contact=contact
    )

