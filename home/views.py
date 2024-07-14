from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from .utils import send_email_with_attachment, zip_folder

def send_email_to_client():
    subject = "This email is from Django Server"
    message = "This email is a test message from the server"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["imailvirat@gmail.com"]

    send_mail(subject, message, from_email, recipient_list)

def send_email(request):
    subject = "Python (Selenium) Assignment - Virat Gupta"
    message = (
        "Dear Team,\n\n"
        "Please find attached the screenshots of the form submissions in the zip file. "
        "The documentation for this assignment is available in the README file of my GitHub repository (13virat). "
        "You can access the repository using the following link: https://github.com/13virat/email.\n\n"
        "Best regards,\n"
        "Virat Gupta"
    )
    recipient_list = ["tech@themedius.ai"]
    cc_list = ["hr@themedius.ai"]
    folder_path = f"{settings.BASE_DIR}/selenium"
    zip_path = f"{settings.BASE_DIR}/my_folder.zip"
    
    # Zip the folder
    zip_folder(folder_path, zip_path)
    
    # Send the email with the zipped folder
    send_email_with_attachment(subject, message, recipient_list, zip_path, cc_list)
    
    return HttpResponse("Email sent with folder!")

def home_view(request):
    return render(request, "home/index.html")
