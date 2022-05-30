from django.contrib.auth import get_user_model  # ссылка на актуальную модель пользователя
from django.contrib.auth.forms import UserCreationForm

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