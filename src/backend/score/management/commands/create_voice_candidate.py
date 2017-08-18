# django modules
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

# local project modules
from score.models import Candidate, Team


class Command(BaseCommand):
    help = 'create the voice TV mentor account'

    def add_arguments(self, parser):
        parser.add_argument('username')
        # parser.add_argument('email')
        parser.add_argument('password')
        parser.add_argument('team_name')

    def handle(self, *args, **options):
        try:
            User.objects.get(username=options['username'])
        except User.DoesNotExist:
            try:
                team = Team.objects.get(name=options['team_name'])
            except Team.DoesNotExist:
                raise CommandError(
                    'You must create a team before creating a candidate'
                )

            user = User.objects.create_user(
                username=options['username'],
                # email=options['email'],
                password=options['password'],
                is_active=False
            )

            Candidate.objects.create(user=user, team=team)
            return

        raise CommandError('This candidate account already existed.')