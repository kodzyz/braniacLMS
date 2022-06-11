from django.core.management import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = (
        "This command using for call 'makemessages' with using flags:\n"
        "--locale, --ignore and --no-location"
    )

    def handle(self, *args, **options):
        call_command("makemessages", "--locale=ru", '--ignore=venv', "--no-location")

# python manage.py makemessages -l ru -i venv
# python manage.py compilemessages -i venv