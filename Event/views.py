from django.shortcuts import render

from .models import Competition

# Create your views here.


def showcompetition(request):
    competition  = Competition.objects.all()
    context ={
        'all_competition': competition
    }
    return render(request,'Event/showcompetition.html', context)
