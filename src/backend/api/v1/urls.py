# django modules
from django.conf.urls import url

# django third-party modules
from rest_framework_jwt.views import obtain_jwt_token

# local project modules
from . import views as api_views


urlpatterns = [
    url(r'^authenticate/$', obtain_jwt_token),

    url(r'^usertype/$', api_views.UserTypeView.as_view())
]
