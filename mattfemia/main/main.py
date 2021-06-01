from flask import Flask, Blueprint, url_for, render_template, redirect, request, flash
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

    # Redirect http to https
    if os.environ['FLASK_ENV'] == 'production':
        if request.url.startswith('http://'):
            url = request.url.replace("http://", "https://", 1)
            code = 301
            return redirect(url, code=code)

    contact = ContactForm()
    if contact.validate_on_submit():
        
        # Get form data
        name = contact.name.data
        email = contact.email.data
        message = contact.message.data

        # Send Message
        msg = Message(subject=f"Contact Request <{name}>",
                      sender="femiafreelance@gmail.com",
                      recipients=["femiafreelance@gmail.com"],
                      body=f"Sender Name: {name}\nSend Email: {email}\n\nBEGIN MESSAGE--------------\n\n{message}\n\nEND MESSAGE--------------")
        mail.send(msg)
        
        flash("Message sent! Thanks for reaching out. I will be in touch soon.", "secondary")
        return redirect(url_for('main.index'))

    return render_template(
        'main/index.html',
        contact=contact
    )

