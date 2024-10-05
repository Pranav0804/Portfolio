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


def index(request):
    return render(request, 'index.html')
