# django modules
from django.core.management.base import BaseCommand, CommandError

# local project modules
from score.models import Activity, Mentor, Score


class Command(BaseCommand):
    help = 'create the voice TV show score for single activity'

    def add_arguments(self, parser):
        parser.add_argument('candidate_username')
        parser.add_argument('song_name')
        parser.add_argument('mentor_username')
        parser.add_argument('score')

    def handle(self, *args, **options):
        try:
            activity = Activity.objects.get(
                candidate__user__username=options['candidate_username'],
                song_name=options['song_name']
            )
            mentor = Mentor.objects.get(
                user__username=options['mentor_username']
            )
        except Activity.DoesNotExist:
            raise CommandError('The activity does not exist, create it first')
        except Mentor.DoesNotExist:
            raise CommandError('The mentor does not exist, create it first')

        Score.objects.create(
            activity=activity,
            mentor=mentor,
            score=options['score']
        )
