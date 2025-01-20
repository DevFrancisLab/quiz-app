from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='quiz-home'),
    path('leaderboard/', views.leaderboard, name='quiz-leaderboard'),
]