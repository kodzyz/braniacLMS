from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


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
                'data': '2822-01-01'
            },
            {
                'title': 'Новость два',
                'preview': 'Превью к новости два',
                'data': '2822-01-02'
            },
            {
                'title': 'Новость три',
                'preview': 'Превью к новости три',
                'data': '2822-01-03'
            },
            {
                'title': 'Новость четыре',
                'preview': 'Превью к новости четыре',
                'data': '2822-01-04'
            },
            {
                'title': 'Новость пять',
                'preview': 'Превью к новости пять',
                'data': '2822-01-05'
            },
            {
                'title': 'Новость шесть',
                'preview': 'Превью к новости шесть',
                'data': '2822-01-06'
            },
        ]
        return context_data