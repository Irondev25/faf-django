from django.core.mail import send_mail
from django.conf import settings

def email(recipient,username,password):
    subject = 'Faculty Achivement Forum'
    message = 'Welcome to faculty achivement forum\nusername: '+username;
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [recipient,]

    send_mail(subject,message,email_from,recipient_list)
    
