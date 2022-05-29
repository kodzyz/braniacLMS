from django.contrib import admin
from mainapp.models import News, Course, Lesson, CoursesTeachers
from django.utils.html import format_html

# Register your models here.

# Зарегистрируйте модель пользователя
# admin.site.register(News)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(CoursesTeachers)


@admin.register(News)
class NewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'deleted')  # 'slug' несуществующе поле решаемое в отдельной ф-и
    ordering = ('pk',)  # сортировка по умолчанию

    def slug(self, obj):
        return format_html(
            '<a href="{}" target="_blank">{}</a>',  # перелинковка ссылка на новость
            obj.title.lower().replace(' ', '-'),
            obj.title
        )

    slug.short_description = 'Слаг'  # описание поля
