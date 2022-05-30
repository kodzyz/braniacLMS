from django.contrib.auth import get_user_model  # ссылка на актуальную модель пользователя
from django import forms
from django.contrib.auth.forms import UserCreationForm


# class StyleFormMixin:
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             print(field.widget)
#             if isinstance(field.widget, forms.widgets.CheckboxInput):
#                 field.widget.attrs['class'] = 'form-check-input'
#             elif isinstance(field.widget, forms.DateTimeInput):
#                 field.widget.attrs['class'] = 'form-control flatpickr-basic'
#             elif isinstance(field.widget, forms.TimeInput):
#                 field.widget.attrs['class'] = 'form-control flatpickr-time'
#             elif isinstance(field.widget, forms.widgets.SelectMultiple):
#                 field.widget.attrs['class'] = 'select2 form-control select2-multiple'
#             else:
#                 field.widget.attrs['class'] = 'form-control'


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # обязательные параметры
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'age',
            'avatar'
        )
