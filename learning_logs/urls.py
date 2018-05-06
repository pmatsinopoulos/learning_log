from django.conf.urls import url
from . import views

app_name = 'reviews'

urlpatterns = [
    # Home page
    url('^$', views.index, name='index'),

    # Show all topics
    url('^topics/$', views.topics, name='topics'),

    # Show specific topic
    url('^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
]
