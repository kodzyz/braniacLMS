from django.test import TestCase
from http import HTTPStatus

# Create your tests here.
from django.urls import reverse


class StaticPagesSmokeTest(TestCase):

    def test_page_index_open(self):
        url = reverse('mainapp:index')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.OK)  # 200 'Request fulfilled, document follows'

    def test_page_contacts_open(self):
        url = reverse('mainapp:contacts')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.OK)

# python manage.py test
# один метод -> python manage.py test mainapp.tests.StaticPagesSmokeTest.test_page_contacts_open
