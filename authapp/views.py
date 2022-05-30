from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView

# Create your views here.
from authapp.forms import CustomUserCreationForm
from authapp.models import User


class CustomLoginView(LoginView):
    template_name = 'authapp/login.html'  # http://127.0.0.1:8000/authapp/login/
    extra_context = {
        'title': 'Вход пользователя'
    }


class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('mainapp:index')



# class RegisterView(TemplateView):
#     template_name = 'authapp/register.html'
#     extra_context = {
#         'title': 'Регистрация пользователя'
#     }
#
#     def post(self, request, *args, **kwargs):
#         try:
#             print(type(request.POST))
#             if all(
#                     (
#                             request.POST.get('username'),
#                             request.POST.get('email'),
#                             request.POST.get('password1'),
#                             request.POST.get('password2'),
#                             request.POST.get('first_name'),
#                             request.POST.get('last_name'),
#                             request.POST.get('password1') == request.POST.get('password2'),
#                     )
#             ):
#                 new_user = User.objects.create(
#                     username=request.POST.get('username'),
#                     first_name=request.POST.get('first_name'),
#                     last_name=request.POST.get('last_name'),
#                     email=request.POST.get('email'),
#                     age=request.POST.get('age') if request.POST.get('age') else 0,
#                     avatar=request.FILES.get('avatar')
#                 )
#                 new_user.set_password(request.POST.get('password1'))
#                 new_user.save()
#                 messages.add_message(request, messages.INFO, 'Регистрация прошло успешно')
#                 return HttpResponseRedirect(reverse('authapp:login'))
#             else:
#                 messages.add_message(
#                     request,
#                     messages.WARNING,
#                     'Что-то пошло не так!'
#                 )
#         except Exception as ex:
#             messages.add_message(
#                 request,
#                 messages.WARNING,
#                 'Что-то пошло не так!'
#             )
#             return HttpResponseRedirect(reverse('authapp:register'))
#

class CustomLogoutView(LogoutView):
    pass


class EditView(TemplateView):
    template_name = 'authapp/edit.html'

    extra_context = {
        'title': 'Регистрация пользователя'
    }

    def post(self, request, *args, **kwargs):
        if request.POST.get('username'):
            request.user.username = request.POST.get('username')

        if request.POST.get('first_name'):
            request.user.first_name = request.POST.get('first_name')

        if request.POST.get('last_name'):
            request.user.last_name = request.POST.get('last_name')

        if request.POST.get('age'):
            request.user.age = request.POST.get('age')

        if request.POST.get('email'):
            request.user.email = request.POST.get('email')

        # if request.POST.get('password'):
        #     request.user.set_password(request.POST.get('password')) # хеш авто

        request.user.save()
        return HttpResponseRedirect(reverse('authapp:edit'))
