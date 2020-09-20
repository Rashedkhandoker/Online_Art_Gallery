from django.shortcuts import render
from .models import Exhibition

# Create your views here.
def showevent(request):
    exhibition = Exhibition.objects.all()
    context ={
        'all_exhibition': exhibition
    }
    return render(request,'Event/showevent.html', context)
