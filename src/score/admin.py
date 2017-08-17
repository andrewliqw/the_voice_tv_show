# django modules
from django.contrib import admin

# local project modules
from . import models


@admin.register(models.Mentor)
class MentorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Candidate)
class CandidateAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Score)
class ScoreAdmin(admin.ModelAdmin):
    pass
