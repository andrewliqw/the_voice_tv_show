# django modules
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

# local project modules
from score.models import Mentor


class Command(BaseCommand):
    help = 'create the voice TV mentor account'

    def add_arguments(self, parser):
        parser.add_argument('username')
        # parser.add_argument('email')
        parser.add_argument('password')

    def handle(self, *args, **options):
        try:
            User.objects.get(username=options['username'])
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=options['username'],
                # email=options['email'],
                password=options['password']
            )
            Mentor.objects.create(user=user)
            return

        raise CommandError('This mentor account already existed.')