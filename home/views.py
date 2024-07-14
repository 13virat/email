# from django.shortcuts import redirect, render
# from django.http import HttpResponse
# from .utils import send_email_to_client
# # Create your views here.
# def send_email(request):
#     send_email_to_client()
#     return HttpResponse("Email sent!")
# def home_view(request):
#     return render(request, 'home/index.html')
# home/views.py

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

def send_email_to_client():
    subject = "This email is from Django Server hiii "
    message = "This email is test message server changed the message "
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["imailvirat@gmail.com"]

    send_mail(subject, message, from_email, recipient_list)

def send_email(request):
    send_email_to_client()
    return HttpResponse("Email sent!")

def home_view(request):
    return render(request, 'home/index.html')
