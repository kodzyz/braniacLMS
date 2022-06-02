from django.db import models
from django.contrib.auth.models import AbstractUser

from mainapp.models import NULLABLE


# Create your models here.

# новый пользователь
class User(AbstractUser):
    email = models.EmailField(blank=True, verbose_name='Email', unique=True)  # переопределеие свойства email
    age = models.PositiveSmallIntegerField(verbose_name='Возвраст', **NULLABLE)  # null=True можно не заполнять
    avatar = models.ImageField(upload_to='users', **NULLABLE)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

