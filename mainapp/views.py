from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import datetime


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = [
            {
                'title': 'Новость раз',
                'preview': 'Превью к новости раз',
                'date': datetime.now()  # datetime.now().strftime('%d.%m.%Y')
            },
            {
                'title': 'Новость два',
                'preview': 'Превью к новости два',
                'date': datetime.now()
            },
            {
                'title': 'Новость три',
                'preview': 'Превью к новости три',
                'date': datetime.now()
            },
            {
                'title': 'Новость четыре',
                'preview': 'Превью к новости четыре',
                'date': datetime.now()
            },
            {
                'title': 'Новость пять',
                'preview': 'Превью к новости пять',
                'date': datetime.now()
            },
            {
                'title': 'Новость шесть',
                'preview': 'Превью к новости шесть',
                'date': datetime.now()
            },
        ]
        return context_data