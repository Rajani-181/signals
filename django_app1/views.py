from django.http import HttpResponse
from django.shortcuts import render

from . import customSignals
from django_app1.models import Post


# Create your views here.

def home(request):
    p = 10 / 0
    return HttpResponse("Hello")


def home1(request):
    # customSignals.notification.send(sender=request, request=request,
    #                                 user=['rajani','raj'])
    customSignals.notification.send_robust(sender=request, request=request,
                                    user=['rajani','raj'])
    return HttpResponse("This is Home signal")
