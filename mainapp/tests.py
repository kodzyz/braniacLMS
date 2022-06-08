from django.test import TestCase, Client
from http import HTTPStatus

# Create your tests here.
from django.urls import reverse

from authapp.models import User
from mainapp.models import News


class StaticPagesSmokeTest(TestCase):

    def test_page_index_open(self):
        url = reverse('mainapp:index')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.OK)  # 200 'Request fulfilled, document follows'

    def test_page_contacts_open(self):
        url = reverse('mainapp:contacts')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.OK)


class NewsTestCase(TestCase):  # функцональный тест

    def setUp(self) -> None:  # выполнение команд перед тестом
        # super().setUp()
        for i in range(10):
            News.object.create(  # -> заполнение бд
                title=f'News{i}',
                preamble=f'Intro{i}',
                body=f'Body{i}'
            )
        # авторизованный клиент
        User.objects.create_superuser(username='django', password='geekbrains')  # создаем автор. пользователя
        self.client_with_auth = Client()
        auth_url = reverse('authapp:login')  # адрес на авторизацию
        self.client_with_auth.post(
            auth_url,
            {'username': 'django', 'password': 'geekbrains'}
        )

    def test_open_page(self):
        url = reverse('mainapp:news')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.OK)

    def test_failed_open_add_by_anonym(self):  # неудачное открытие неавторизованным страницы редактирования
        url = reverse('mainapp:news_create')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.FOUND)  # 302

    def test_create_news_item_by_admin(self):
        news_count = News.object.all().count()

        url = reverse('mainapp:news_create')
        result = self.client_with_auth.post(
            url,
            data={
                'title': 'Test news',
                'preamble': 'Test intro',
                'body': 'Test body'
            }
        )

        self.assertEqual(result.status_code, HTTPStatus.FOUND)

        self.assertEqual(News.object.all().count(), news_count + 1)
