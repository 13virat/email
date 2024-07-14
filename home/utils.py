import os
import zipfile
from django.core.mail import EmailMessage
from django.conf import settings

def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

def send_email_with_attachment(subject, message, recipient_list, file_path, cc_list=None):
    mail = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=recipient_list,
        cc=cc_list
    )
    mail.attach_file(file_path)
    mail.send()
