__author__ = 'epagua'

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from payment import views

urlpatterns = [
    url(r'^tipoU/$', views.TypeUserList.as_view()),
    url(r'^tipoUsuD/(?P<pk>[0-9]+)/$', views.TypeUserDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)