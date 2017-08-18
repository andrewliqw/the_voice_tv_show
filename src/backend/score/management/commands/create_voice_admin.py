from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'create the voice TV show admin account'

    def add_arguments(self, parser):
        parser.add_argument('username')
        parser.add_argument('email')
        parser.add_argument('password')

    def handle(self, *args, **options):
        try:
            User.objects.get(username=options['username'])
        except User.DoesNotExist:
            User.objects.create_superuser(
                username=options['username'],
                email=options['email'],
                password=options['password']
            )
            return

        raise CommandError('This admin account already existed.')