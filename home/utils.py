from django.core.mail import send_mail
from django.conf import settings


def send_email_to_client():
    subject = "This email is from Django Server"
    message = "This email is test message server"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["imailvirat@gmail.com"]

    send_mail(subject, message, from_email, recipient_list)
