from django.conf.urls import url
from . import views

app_name = 'baseapp'

urlpatterns = [
    url('^roulette', views.roulette, name='roulette'),
    url('^description', views.description, name='description'),
    url('^question', views.question, name='question'),
    url('^afteranswer', views.afteranswer, name='afteranswer'),
    url('^leaderboard', views.leaderboard, name='leaderboard'),
]
