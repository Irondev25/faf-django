from django.core.mail import send_mail
import os

"""
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def email(recipient,username,password):
    message = Mail(from_email='facultyachivementforum@gmail.com',to_emails=recipient,subject='Welcome to Faculty Achivement Forum',html_content='<h1>Faculty Achivement Forum</h1><p><b>username</b>{0}</p>'.format(username))
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
"""

def email(recipient,username,password):
    subject = 'Faculty Achivement Forum'
    message = 'Welcome to faculty achivement forum\nusername: '+username;
    email_from = 'facultyachivementforum@gmail.com'
    recipient_list = [recipient,]

    send_mail(subject,message,email_from,recipient_list)