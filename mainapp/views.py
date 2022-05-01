from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# первый контроллер
def hello_world(request):
    return HttpResponse("Hello world!")

# def blog(request):
#     return HttpResponse("I am blog")

def blog(request, **kwargs):
    return HttpResponse(f"{kwargs}")