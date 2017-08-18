# django modules
from django.conf.urls import url
from django.contrib.auth import views as auth_views

# local project modules
from . import views


app_name = 'score'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(
        r'^login/$',
        auth_views.LoginView.as_view(
            template_name='score/login.html'
        ),
        name='login',
    ),

    url(
        r'^logout/$',
        auth_views.logout_then_login,
        name='logout'
    ),

    url(
        r'^admin/$',
        views.AdminView.as_view(),
        name='admin_view'
    ),

    url(
        r'mentor/$',
        views.MentorView.as_view(),
        name='mentor_view'
    ),

    url(
        r'^team/(?P<team_id>[0-9]+)/$',
        views.TeamView.as_view(),
        name='team_view'
    ),

    url(
        r'^candidate/(?P<candidate_id>[0-9]+)/$',
        views.CandidateView.as_view(),
        name='candidate_view'
    )
]
