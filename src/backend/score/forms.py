# django modules
from django import forms

# local project modules
from score.models import Team


class AdminSelectForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        choices = []
        for team in Team.objects.all():
            choices.append((team.id, team.name))

        self.fields['teams'] = forms.MultipleChoiceField(
            choices=choices
        )
