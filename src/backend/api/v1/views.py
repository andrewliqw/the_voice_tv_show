# python std modules
import json

# django modules
# from django.http import JsonResponse

# django third-party modules
from rest_framework.response import Response
from rest_framework.views import APIView

from score.models import Team

class UserTypeView(APIView):
    def get(self, request, format=None):
        user_type = None
        if request.user.is_superuser:
            user_type = 'admin'
        else:
            user_type = 'mentor'

        return Response({'user_type': user_type})


class AllTeamNamesView(APIView):
    def get(self, request, format=None):
        all_names = []
        for team in Team.objects.all():
            all_names.append((team.id, team.name))

        return Response(all_names)


class TeamScoresView(APIView):
    def post(self, request, format=None):
        team_ids = request.data

        teams = Team.objects.filter(id__in=team_ids)
        team_score = []
        for team in teams:
            team_score.append({
                'id': team.id,
                'name': team.name,
                'average_score': team.average_score
            })

        return Response(team_score)
