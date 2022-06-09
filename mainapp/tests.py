from django.test import TestCase, Client
from http import HTTPStatus
from django.core import mail
# Create your tests here.
from django.urls import reverse

from authapp.models import User
from mainapp.models import News


class StaticPagesSmokeTest(TestCase):

    def test_page_index_open(self):
        url = reverse('mainapp:index')  # адрес для открытия
        result = self.client.get(url)  # ответ от клиента

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


class EmailTest(TestCase):
    def test_send_email(self):
        mail.send_mail('Subject here', 'Here is the message.',
                       'from@example.com', ['to@example.com'],
                       fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')


class ContactTests(TestCase):  # тест не работает !!! а celery работает
    def test_post(self):
        with self.captureOnCommitCallbacks(execute=True) as callbacks:
            response = self.client.post(
                '/mainapp/contacts/',
                {'message_body': 'I like your site'},
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(callbacks), 1)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Contact Form')
        self.assertEqual(mail.outbox[0].body, 'I like your site')


# python manage.py test
