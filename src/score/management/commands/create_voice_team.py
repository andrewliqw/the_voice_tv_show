# django modules
from django.core.management.base import BaseCommand, CommandError

# local project modules
from score.models import Mentor, Team


class Command(BaseCommand):
    help = 'create the voice TV show team'

    def add_arguments(self, parser):
        parser.add_argument('team_name')
        parser.add_argument('mentor_username')

    def handle(self, *args, **options):
        try:
            Team.objects.get(name=options['team_name'])
        except Team.DoesNotExist:
            try:
                mentor = Mentor.objects.get(
                    user__username=options['mentor_username']
                )
            except Mentor.DoesNotExist:
                raise CommandError(
                    'You must create the given mentor account before creating team'
                )

            Team.objects.create(
                name=options['team_name'],
                mentor=mentor
            )
            return

        raise CommandError('This team already existed.')