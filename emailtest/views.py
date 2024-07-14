from django.core.mail import send_mail

send_mail(
    "Subject here",
    "Here is the message.",
    "testingservervirat@gmail.com",
    ["viratgupta1314@gmail.com"],
    fail_silently=False,
)
