Python (Selenium) Assignment Documentation
==========================================

Objectives
----------

1.  **Submit the details on the Google form provided via code.**
2.  **Capture a screenshot (in PDF, JPG, or PNG format) of the confirmation page.**
3.  **Send the captured screenshot via email using Django's email functionality.**

### Google Form Link

<https://forms.gle/WT68aV5UnPajeoSc8>

### Email Instructions

-   **Subject**: Python (Selenium) Assignment - [Your Name]
-   **To**: tech@themedius.ai
-   **CC**: hr@themedius.ai

* * * * *

Solution Overview
-----------------

The solution is divided into two parts:

1.  **Automating Google Form Submission using Selenium**
2.  **Sending Email with the Screenshot of Confirmation Page using Django**

### 1\. Automating Google Form Submission using Selenium

We created a Python script using Selenium to automate the form submission process. This script reads the details from a CSV file, fills out the form, submits it, and captures screenshots of the confirmation page.

#### Prerequisites

-   Install `selenium` using `pip install selenium`
-   Download and place the `chromedriver` in your system path or specify the path in the script.

#### Script: `fillform.py`

python

Copy code

`import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set the path to the chromedriver
chrome_driver_path = "/usr/local/bin/chromedriver"

# Create a service object
service = Service(chrome_driver_path)

# Create options object and add necessary options
chrome_options = Options()

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the Google Form
url = "https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform"

# Open the URL
driver.get(url)

def fill_form(fullname, contact, email, address, pincode, dob, gender, code, index):
    # Wait for the form elements to be present
    time.sleep(2)  # wait for the form to load

    # Find all input elements by class name
    inputs = driver.find_elements(By.CLASS_NAME, "whsOnd")

    # List of input values
    inputs_array = [fullname, contact, email, pincode, dob, gender, code]

    for i in range(len(inputs_array)):
        # Clear the input field
        inputs[i].clear()
        # Enter the data into the input field
        inputs[i].send_keys(inputs_array[i])

    # Find the textarea element by class name
    address_input = driver.find_element(By.CLASS_NAME, "KHxj8b")
    # Clear the textarea field
    address_input.clear()
    # Enter the data into the textarea field
    address_input.send_keys(address)

    # Take a screenshot before submitting the form
    driver.save_screenshot(f'form_filled_{index}_before.png')

    # Optionally, you may want to submit the form
    submit_button = driver.find_element(By.CLASS_NAME, "NPEfkd")
    submit_button.click()

    # Take a screenshot after submitting the form
    driver.save_screenshot(f'form_filled_{index}_after.png')

    # Click on the link to submit another response
    another_response = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    another_response.click()

# Read the CSV file and fill the form for each entry
with open("form_entries.csv", mode='r') as file:
    reader = csv.reader(file, delimiter=',')
    for index, row in enumerate(reader):
        fill_form(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], index)

print("Success")

# Add a delay to keep the browser open
time.sleep(10)

# Close the browser
driver.quit()`

### 2\. Sending Email with the Screenshot using Django

We created Django utility functions to zip a folder containing the screenshots and send it via email.

#### Prerequisites

-   Install `Django` using `pip install django`
-   Configure the email settings in `settings.py`.

#### Django Configuration

Add the following settings to `settings.py`:

`EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password'`

#### Utility Function: `home/utils.py`

`import os
import zipfile
from django.core.mail import EmailMessage
from django.conf import settings

def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

def send_email_with_attachment(subject, message, recipient_list, file_path):
    mail = EmailMessage(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=recipient_list)
    mail.attach_file(file_path)
    mail.send()`

#### View: `home/views.py`

`from django.core.mail import send_mail
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
    subject = "Python (Selenium) Assignment - Virat Gupta]"
    message = "Please find the attached screenshots of the form submissions."
    recipient_list = ["tech@themedius.ai"]
    cc_list = ["hr@themedius.ai"]
    folder_path = f"{settings.BASE_DIR}/screenshots"
    zip_path = f"{settings.BASE_DIR}/screenshots.zip"

    # Zip the folder
    zip_folder(folder_path, zip_path)

    # Send the email with the zipped folder
    send_email_with_attachment(subject, message, recipient_list + cc_list, zip_path)

    return HttpResponse("Email sent with folder!")

def home_view(request):
    return render(request, "home/index.html")`

### 3\. Submission Requirements

#### Share the GitHub repository containing your code:

1.  Create a GitHub repository.
2.  Add your code to the repository.
3.  Share the repository link.

#### Email your submission:

1.  **The source code**:
    -   Include all the Python files (`fillform.py`, Django project files, etc.)
2.  **A brief documentation outlining your approach**:
    -   This README file.
3.  **The screenshot of the confirmation page**:
    -   Ensure the screenshots are saved in the `screenshots` folder and zipped.

* * * * *

Running the Solution
--------------------

### Step 1: Run the Selenium Script

`python fillform.py`

### Step 2: Start the Django Server

`python manage.py runserver`

### Step 3: Send the Email

1.  Navigate to `http://127.0.0.1:8000/`
2.  Click on the "SEND MAIL" button to trigger the email sending process.

* * * * *
