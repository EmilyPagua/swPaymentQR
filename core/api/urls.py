from django.conf.urls import include, url, patterns
from rest_framework.authtoken.models import Token


urlpatterns = patterns('core.api.views',
    url(r'^hola_mundo_rest/(?P<nombre>\w+)/$', 'hola_mundo'),
    url(r'^usuarios/$', 'user_list',name='usuarios'),
    url(r'^usuarios/(?P<id>\d+)/$', 'user_detail', name='usuario'),
    url(r'^todo/$', 'todo_list', name='todo' ),
    url(r'^todo/(?P<id>\d+)/$', 'todo_detail', name='todo'),

)
