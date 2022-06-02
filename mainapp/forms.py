from django import forms

from mainapp.models import CourseFeedback


class CourseFeedbackForm(forms.ModelForm):

    class Meta:
        model = CourseFeedback
        fields = ('course', 'user', 'rating', 'feedback',)
        widgets = {  # пользователь и курс скрыты
            'course': forms.HiddenInput(),
            'user': forms.HiddenInput(),
            #'rating': forms.HiddenInput()
        }

    def __init__(self, *args, course=None, user=None, **kwargs):  # предустановка скрытых полей
        super().__init__(*args, **kwargs)
        if course and user:  # переменные для инициализации формы
            self.fields['course'].initial = course.pk
            self.fields['user'].initial = user.pk
