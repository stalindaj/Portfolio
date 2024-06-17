from django.shortcuts import render
from django.http import HttpResponse  # Correct import statement for HttpResponse

def home(request):
    return HttpResponse("Hello, World")  # Correct usage of HttpResponse
