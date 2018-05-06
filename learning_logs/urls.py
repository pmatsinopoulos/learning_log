from django.conf.urls import url
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    url('^$', views.index, name='index'),

    # Show all topics
    url('^topics/$', views.topics, name='topics'),

    # Show specific topic
    url('^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    url('^topics/new$', views.new_topic, name='new_topic'),

    url('^topics/(?P<topic_id>\d+)/entries/new$', views.new_entry, name='new_entry'),

    # /topics/<topic-id>/entries/<entry-id>/edit
    url('^topic/(?P<topic_id>\d+)/entries/(?P<entry_id>\d+)/edit$', views.edit_entry, name='edit_entry'),
]
