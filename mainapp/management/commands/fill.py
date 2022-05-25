from django.core.management import BaseCommand

from mainapp.models import News

class Command(BaseCommand):

    def handle(self, *args, **options):
        #print('hello terminal')  # python manage.py fill -> hello terminal
        for i in range(10):
            News.object.create(
                title=f'title#{i}',
                preamble=f'preamble#{i}',
                body='some body'
            )


