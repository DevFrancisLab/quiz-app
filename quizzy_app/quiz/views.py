from django.shortcuts import render
from .models import Results

def home(request):
    return render(request,'quiz/home.html', {'title': 'Home'})

def leaderboard(request):
    context = {
        'results': Results.objects.all()
    }
    return render(request,'quiz/leaderboard.html', context)
