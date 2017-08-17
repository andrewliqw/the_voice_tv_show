# django modules
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse
from django.views import View

# local project modules
from . import models
from .forms import AdminSelectForm


# candidate could not login because is_acitve is False
@login_required()
def index(request):
    if request.user.is_superuser:
        # return HttpResponse('You are admin.')
        return HttpResponseRedirect(reverse('score:admin_view'))
    else:
        return HttpResponseRedirect(reverse('score:mentor_view'))


class AdminView(LoginRequiredMixin, View):
    template_name = 'score/admin_view.html'
    form_class = AdminSelectForm
    default_context = {
        'title': 'admin view'
    }

    def get(self, request):
        if not request.user.is_superuser:
            return HttpResponse('You are not an admin')

        form = AdminSelectForm()
        all_teams = models.Team.objects.all()
        context = {
            'form': form,
            'all_teams': all_teams
        }
        context.update(self.default_context)

        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        form = AdminSelectForm(request.POST)
        all_teams = None
        if form.is_valid():
            team_ids = form.cleaned_data['teams']
            all_teams = models.Team.objects.filter(id__in=team_ids)

        context = {
            'form': form,
            'all_teams': all_teams
        }
        context.update(self.default_context)
        return TemplateResponse(request, self.template_name, context)


class MentorView(LoginRequiredMixin, View):
    template_name = 'score/mentor_view.html'
    default_context = {'title': 'Mentor view'}

    def get(self, request):
        mentor = models.Mentor.objects.get(user=request.user)
        context = {'mentor': mentor}
        context.update(self.default_context)
        return TemplateResponse(request, self.template_name, context)


class TeamView(LoginRequiredMixin, View):
    template_name = 'score/team_view.html'
    default_context = {'title': 'Team scores'}

    def get(self, request, team_id):
        team = models.Team.objects.get(id=team_id)
        context = {'team': team}
        context.update(self.default_context)
        return TemplateResponse(request, self.template_name, context)


class CandidateView(LoginRequiredMixin, View):
    template_name = 'score/candidate_view.html'
    default_context = {'title': 'Candidate scores'}

    def get(self, request, candidate_id):
        candidate = models.Candidate.objects.get(id=candidate_id)

        if not request.user.is_superuser:
            if candidate.team.mentor.user != request.user:
                return HttpResponse(
                    'You are not admin or the montor of this candidate.'
                )

        context = {'candidate': candidate}
        context.update(self.default_context)
        return TemplateResponse(request, self.template_name, context)
