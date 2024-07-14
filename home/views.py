from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from .utils import send_email_with_attachment

def send_email_to_client():
    subject = "This email is from Django Server"
    message = "This email is a test message from the server"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["imailvirat@gmail.com"]

    send_mail(subject, message, from_email, recipient_list)

def send_email(request):
    subject = "This email is from Django Server hiii"
    message = "This email is a test message from the server, changed the message"
    recipient_list = ["imailvirat@gmail.com"]
    file_path = f"{settings.BASE_DIR}/hi.xlsx"
    send_email_with_attachment(subject, message, recipient_list, file_path)
    return HttpResponse("Email sent!")

def home_view(request):
    return render(request, "home/index.html")
