from django.conf.urls import include, url, patterns
from rest_framework.authtoken.models import Token


urlpatterns = patterns('core.api.views',
    url(r'^usuarios/$', 'user_list',name='usuarios'),
    url(r'^usuarios/(?P<id>\d+)/$', 'user_detail', name='usuario'),
    url(r'^todo/$', 'todo_list', name='todo' ),
    url(r'^todo/(?P<id>\d+)/$', 'todo_detail', name='todo'),
    url(r'^typecard/$', 'typecard_list', name='tarjeta' ),
    url(r'^typecard/(?P<id>\d+)/$', 'typecard_detail', name='tarjeta'),

    url(r'^card/$', 'card_list', name='card'),
    url(r'^card/(?P<id>\d+)/$', 'card_detail', name='card'),

)
