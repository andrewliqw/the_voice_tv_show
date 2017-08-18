from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Mentor(models.Model):
    class Meta:
        verbose_name = 'mentor'
        verbose_name_plural = 'mentors'

    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return 'Mentor:{}'.format(self.user.username)


class Team(models.Model):
    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'teams'

    name = models.CharField(max_length=100)
    mentor = models.ForeignKey(
        Mentor,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    @property
    def average_score(self):
        total = 0
        n = 0
        for candidate in self.candidate_set.all():
            total = total + candidate.average_score
            n = n + 1
        return total / n if n !=0 else 0


class Candidate(models.Model):
    class Meta:
        verbose_name = 'candidate'
        verbose_name_plural = 'candidates'

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    team = models.ForeignKey(
        Team,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return 'C:{}'.format(self.user.username)

    @property
    def average_score(self):
        total = 0
        n = 0
        for activity in self.activity_set.all():
            total = total + activity.average_score
            n = n + 1

        return total / n if n != 0 else 0

    @property
    def team_average_score(self):
        total = 0
        n = 0
        for candidate in self.team.candidate_set.all():
            total = total + candidate.average_score
            n = n + 1

        return total / n if n != 0 else 0


class Activity(models.Model):
    class Meta:
        verbose_name = 'activity'
        verbose_name_plural = 'activities'
        unique_together = ('candidate', 'song_name')

    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
    performance_date = models.DateField()
    scores = models.ManyToManyField(Mentor, through='Score')

    def __str__(self):
        return self.song_name

    @property
    def average_score(self):
        total = 0
        n = 0
        for score in self.score_set.all():
            total = total + score.score
            n = n + 1

        return total / n if n != 0 else 0


class Score(models.Model):
    class Meta:
        verbose_name = 'score'
        verbose_name_plural = 'scores'

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    score = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return str(self.score)
