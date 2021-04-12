from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_email_task

# Create your views here.


def index(request):

    send_email_task.delay()

    return HttpResponse("Email has been sent!")
