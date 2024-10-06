from django.http import FileResponse
from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import JsonResponse
from threading import Thread
from django.views.decorators.csrf import csrf_exempt
# from .langchain_helper import get_response_from_langchain
import os
import json
import time
# from .settings import EMAIL_HOST_USER

from django.core.mail import send_mail

def index(request):
    return render(request, 'index.html')

def send_confirmation_email(name, email, subject, message):
    # This will run in the background
    send_mail(
        f"Confirmation: {subject}",
        f"Hi {name},\n\nThank you for your message! We will get back to you shortly.\n\nYour message:\n{message}",
        f'pranavsompura0804@gmail.com',  # Replace with your email
        [email],  # Sender's email
        fail_silently=False,
    )

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        print('Sending 1st Mail')

        # Send email to yourself
        send_mail(
            subject,
            f"Message from {name} <{email}>\n\n{message}",
            f'pranavsompura0804@gmail.com',  # Replace with your email
            [f'pranavsompura0804@gmail.com'],  # Add your email here
            fail_silently=False,
        )

        # Return a JSON response immediately after the first email
        response = JsonResponse({'status': 'success'})

        send_confirmation_email(name, email, subject, message)
        # Send confirmation email in the background
        # thread = Thread(target=send_confirmation_email, args=(name, email, subject, message))
        # thread.start()

        return response

    return JsonResponse({'status': 'fail'})