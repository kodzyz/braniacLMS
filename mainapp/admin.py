from django.contrib import admin
from mainapp.models import News, Course, Lesson, CoursesTeachers

# Register your models here.

# Зарегистрируйте модель пользователя
# admin.site.register(News)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CoursesTeachers)


@admin.register(News)
class NewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'deleted', )  # поля для отображения в таблице
