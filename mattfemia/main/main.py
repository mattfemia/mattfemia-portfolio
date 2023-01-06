from flask import Flask, Blueprint, url_for, render_template, redirect, request, flash
from flask import current_app as app
from .forms import *
import boto3
import botocore
from botocore.exceptions import ClientError
import os

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

    # contact = ContactForm()
    # if contact.validate_on_submit():

    #     # Get form data
    #     name = contact.name.data
    #     email = contact.email.data
    #     message = contact.message.data

    #     # Send Message
    #     try:
    #         send_contact_email(email, name, message)
    #     except ClientError as e:
    #         print(e)
    #         flash('An error occurred sending your email', 'danger')
    #         return redirect(url_for('main.index'))
    #     else:
    #         # Reset session_cart data
    #         flash("Message sent! Thanks for reaching out. I will be in touch soon.", "secondary")
    #         return redirect(url_for('main.index'))

    return render_template(
        'main/index.html',
        # contact=contact
    )


def send_contact_email(email, name, message):

    SENDER = "mf@mattfemia.com"
    RECIPIENT = "mf@mattfemia.com"
    AWS_REGION = "us-east-2"
    SUBJECT = f"Contact Request <{name}>"
    CHARSET = "UTF-8"
    BODY_TEXT = (
        f"Sender Name: {name}\nSend Email: {email}\n\nBEGIN MESSAGE--------------\n\n{message}\n\nEND MESSAGE--------------")

    # The HTML body of the email.
    BODY_HTML = f"""
    <html>
    <head></head>
    <body>
        <h3>"Sender Name: {name}</h3>
        Send Email: {email}<h3>
        <h5>BEGIN MESSAGE--------------<h5><br>
        <p>{message}</p><br>
        <h5>END MESSAGE--------------<h5><br>
    </body>
    </html>
     """

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',
                          region_name=AWS_REGION,
                          aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
                          aws_secret_access_key=os.environ.get('AWS_SECRET_KEY'))

    response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
    )

    return


@main.route('/clonotypy', methods=['GET'])
def clonotypy():

    return render_template('main/clonotypy.html')
