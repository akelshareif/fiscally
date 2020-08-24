from os import environ
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(recipient_email, email_subject, content):
    """ Sends an email to all recipients """

    message = Mail(
        from_email='fiscally.email@gmail.com',
        to_emails=recipient_email,
        subject=email_subject,
        html_content=content
    )

    sg = SendGridAPIClient(environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
