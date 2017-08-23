# django modules
# from django.http import JsonResponse

# django third-party modules
from rest_framework.response import Response
from rest_framework.views import APIView


class UserTypeView(APIView):
    def get(self, request, format=None):
        user_type = None
        if request.user.is_superuser:
            user_type = 'admin'
        else:
            user_type = 'mentor'

        return Response({'user_type': user_type})
