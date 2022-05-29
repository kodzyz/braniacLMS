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
    list_display = ('pk', 'title', 'slug', 'deleted')  # 'slug' несуществующе поле решаемое в отдельной ф-и

    def slug(self, obj):
        return obj.title.lower().replace(' ', '-')  # читаемый Url
