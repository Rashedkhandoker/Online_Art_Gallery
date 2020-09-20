from django.shortcuts import render
from .models import Exhibition
from .models import Competition

# Create your views here.
def showevent(request):
    exhibition = Exhibition.objects.all()
    context ={
        'all_exhibition': exhibition
    }
    return render(request,'Event/showevent.html', context)

def showcompetition(request):
    competition  = Competition.objects.all()
    context ={
        'all_competition': competition
    }
    return render(request,'Event/showcompetition.html', context)
