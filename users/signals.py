from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Teacher
from .utils import email

@receiver(post_save,sender=Teacher)
def send_email(sender,instance,created,**kwargs):
    if created:
        mail = instance.email
        username = instance.username
        password = instance.password
        #email(mail,username,password)
