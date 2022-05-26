from django.core.management import BaseCommand

from mainapp.models import News


class Command(BaseCommand):

    def handle(self, *args, **options):
        news_list = []
        for i in range(10):
            news_list.append(News(
                title=f'title#{i}',
                preamble=f'preamble#{i}',
                body='some body'
            ))

        News.object.bulk_create(news_list)  # пакетное создание
