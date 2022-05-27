from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

# Create your views here.
from authapp.models import User


class LoginView(TemplateView):
    template_name = 'authapp/login.html'  # http://127.0.0.1:8000/authapp/login/
    extra_context = {
        'title': 'Вход пользователя'
    }


class RegisterView(TemplateView):
    template_name = 'authapp/register.html'
    extra_context = {
        'title': 'Регистрация пользователя'
    }

    def post(self, request, *args, **kwargs):
        try:
            print(type(request.POST))
            if all(
                    (
                            request.POST.get('username'),
                            request.POST.get('email'),
                            request.POST.get('password1'),
                            request.POST.get('password2'),
                            request.POST.get('first_name'),
                            request.POST.get('last_name'),
                            request.POST.get('password1') == request.POST.get('password2'),
                    )
            ):
                new_user = User.objects.create(
                    username=request.POST.get('username'),
                    first_name=request.POST.get('first_name'),
                    last_name=request.POST.get('last_name'),
                    email=request.POST.get('email'),
                    age=request.POST.get('age') if request.POST.get('age') else 0,
                    avatar=request.FILES.get('avatar')
                )
                new_user.set_password(request.POST.get('password1'))
                new_user.save()
                messages.add_message(request, messages.INFO, 'Регистрация прошло успешно')
                return HttpResponseRedirect(reverse('authapp:login'))
            else:
                messages.add_message(
                    request,
                    messages.WARNING,
                    'Что-то пошло не так!'
                )
        except Exception as ex:
            messages.add_message(
                request,
                messages.WARNING,
                'Что-то пошло не так!'
            )
            return HttpResponseRedirect(reverse('authapp:register'))


# In [1]: from authapp.models import User
# In [2]: user = User.objects.all().first()
# In [3]: user
# Out[3]: <User: django>
# In [4]: user = User.objects.all()
# In [5]: user
# Out[5]: <QuerySet [<User: django>]>


class LogoutView(TemplateView):
    pass


class EditView(TemplateView):
    pass
