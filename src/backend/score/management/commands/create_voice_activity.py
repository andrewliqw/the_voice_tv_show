# django modules
from django.core.management.base import BaseCommand, CommandError

# local project modules
from score.models import Activity, Candidate

class Command(BaseCommand):
    help = 'create the voice TV show activity'

    def add_arguments(self, parser):
        parser.add_argument('candidate_username')
        parser.add_argument('song_name')
        parser.add_argument('performance_date')

    def handle(self, *args, **options):
        try:
            candidate = Candidate.objects.get(
                user__username=options['candidate_username']
            )
            Activity.objects.get(
                candidate=candidate,
                song_name=options['song_name']
            )
        except Candidate.DoesNotExist:
            raise CommandError('The candidate does not exist, create it first')
        except Activity.DoesNotExist:
            Activity.objects.create(
                candidate=candidate,
                song_name=options['song_name'],
                performance_date=options['performance_date']
            )
            return

        raise CommandError('This activity has existed.')
