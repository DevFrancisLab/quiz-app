from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'quiz/home.html', {'title': 'Home'})

def leaderboard(request):
    return render(request,'quiz/leaderboard.html', {'title': 'Leaderboard'})
