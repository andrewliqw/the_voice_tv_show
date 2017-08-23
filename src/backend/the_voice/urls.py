# django modules
from django.conf.urls import include, url
from django.contrib import admin

# local project modules
from . import views


urlpatterns = [
    url(r'^$', views.index),

    url(r'^score/', include('score.urls')),

    url(r'^admin/', admin.site.urls),

    url(r'^api/v1/', include('api.v1.urls'))
]
