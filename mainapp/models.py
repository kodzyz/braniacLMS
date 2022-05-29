from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    deleted = models.BooleanField(default=False, verbose_name='Удален')

    class Meta:
        abstract = True
        ordering = ('-created_at',)  # сортировка в обратном порядке по времени создания

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class NewsManager(models.Manager):

    def delete(self):
        pass

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class News(BaseModel):
    #object = NewsManager()

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    preamble = models.CharField(max_length=1000, verbose_name='Вступление')
    body = models.TextField(verbose_name='Содержимое')
    body_as_markdown = models.BooleanField(default=False, verbose_name='Способ разметки')

    def __str__(self):
        return f'#{self.pk} {self.title}'

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'


# Поля связи

class Course(BaseModel):
    name = models.CharField(max_length=256, verbose_name="Name")
    description = models.TextField(verbose_name="Description", **NULLABLE)  # ** -> распаковка
    description_as_markdown = models.BooleanField(verbose_name="As markdown", default=False)
    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Cost", default=0)
    cover = models.CharField(max_length=25, default="no_image.svg", verbose_name="Cover")

    def __str__(self) -> str:
        return f"{self.pk} {self.name}"

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Связь «один ко многим»
    num = models.PositiveIntegerField(verbose_name="Lesson number")
    title = models.CharField(max_length=256, verbose_name="Name")
    description = models.TextField(verbose_name="Description", **NULLABLE)
    description_as_markdown = models.BooleanField(verbose_name="As markdown", default=False)

    def __str__(self) -> str:
        return f"{self.course.name} | {self.num} | {self.title}"

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ("course", "num")


class CoursesTeachers(BaseModel):
    courses = models.ManyToManyField(Course)  # Связь «многие ко многим»
    name_first = models.CharField(max_length=128, verbose_name="Name")
    name_second = models.CharField(max_length=128, verbose_name="Surname")
    day_birth = models.DateField(verbose_name="Birth date")

    def __str__(self) -> str:
        return "{0:0>3} {1} {2}".format(self.pk, self.name_second, self.name_first)

# миграции - внесение изм в БД в соответствии с определениями в модели

# шаг 1: создаем описание полей
# в терминале:
# -> python manage.py makemigrations

# шаг 2: создать таблицу в БД
# -> python manage.py migrate

#  пустая миграция :
# -> python manage.py makemigrations --empty --name data_load mainapp

# -> pip install ipython
# -> python manage.py shell
# In [1]: from mainapp.models import News
# In [2]: news_item_1 = News(title='news1', preamble='intro1', body='body1')
# In [3]:  news_item_1.save()
# In [4]:  news_item_2 = News.objects.create(title='news2', preamble='intro2', body='body2')
# In [5]: news_item_2
# Out[5]: <News: #2 news2>
# In [6]: news_item_2.pk
# Out[6]: 2
# In [7]: news_item_2.preamble
# Out[7]: 'intro2'
# In [8]: news_item_1.pk
# Out[8]: 1
# In [9]: news_item_2.deleted
# Out[9]: False
# In [10]: news_list = News.objects.all()
# In [11]: news_list
# Out[11]: <QuerySet [<News: #1 news1>, <News: #2 news2>]>
# In [12]: for news_item in news_list:
#     ...:     print(news_item.pk)
#     ...:
# 1
# 2
# In [13]: news_list = News.objects.filter(title='news1')
# In [14]: news_list
# Out[14]: <QuerySet [<News: #1 news1>]>
# In [15]: news_item = news_list[0]
# In [16]: news_item
# Out[16]: <News: #1 news1>
# In [17]: news_item.delete()
# In [18]: news_list = News.objects.filter(title='news1')
# In [19]: news_list
# Out[19]: <QuerySet [<News: #1 news1>]>
# модификаторы
# In [21]: news_list = News.objects.filter(pk__gt=1)
# In [22]: news_list
# Out[22]: <QuerySet [<News: #2 news2>]>
# In [23]: news_list = News.objects.filter(title__contains='1')
# In [24]: news_list
# Out[24]: <QuerySet [<News: #1 news1>]>
# In [26]: news_list = News.objects.filter(title__startswith='1')
# In [27]: news_list
# Out[27]: <QuerySet []>

# python manage.py dumpdata mainapp.News > fix_tmp.json  #(выгружать данные из базы в фикстуры)
# python manage.py loaddata 002_courses # (загрузки данных в БД из фикстуры)
