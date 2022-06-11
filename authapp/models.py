from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from mainapp.models import NULLABLE


# Create your models here.

# новый пользователь
class User(AbstractUser):
    email = models.EmailField(blank=True, verbose_name=_('email'), unique=True)  # переопределеие свойства email
    age = models.PositiveSmallIntegerField(verbose_name=_('age'), **NULLABLE)  # null=True можно не заполнять
    avatar = models.ImageField(upload_to='users', **NULLABLE, verbose_name=_('avatar'))

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

