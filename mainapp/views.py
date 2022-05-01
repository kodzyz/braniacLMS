from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.

# первый контроллер
class HelloWorldView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello world!")



# def hello_world(request):
#     return HttpResponse("Hello world!")


def blog(request, **kwargs):
    return HttpResponse(f"{kwargs}")