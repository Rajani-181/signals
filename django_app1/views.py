from django.http import HttpResponse
from django.shortcuts import render

from django_app1.models import Post


# Create your views here.

def home(request):
    p = 10 / 0
    return HttpResponse("Hello")
