from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class LoginView(TemplateView):
    template_name = 'authapp/login.html'  # http://127.0.0.1:8000/authapp/login/


class RegisterView(TemplateView):
    pass


class LogoutView(TemplateView):
    pass


class EditView(TemplateView):
    pass
