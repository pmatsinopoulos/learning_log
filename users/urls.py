"""Defines URL patterns for users"""

app_name = 'users'

from django.conf.urls import url
from django.contrib.auth.views import login
from users.views import logout, register

urlpatterns = [
    url('^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url('^logout/$', logout, name='logout'),
    url('^register/$', register, name='register')
]
