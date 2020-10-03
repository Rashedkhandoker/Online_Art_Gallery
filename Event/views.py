from django.shortcuts import render, get_object_or_404

from .models import Competition,SubmitCompetition
from .forms import SubmitCompetitionForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def showcompetition(request):
    competition  = Competition.objects.all()
    context ={
        'all_competition': competition
    }
    return render(request,'Event/showcompetition.html', context)




@login_required()
def submitart(request):
    message = ""
    form =SubmitCompetitionForm()

    if request.method == "POST":
        form = SubmitCompetitionForm(request.POST,request.FILES)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            submitart= form.save(commit=False)

            submitart.user = request.user
            submitart.save()
            message = "Artwork is submitted to Competition"
            form = SubmitCompetitionForm()

    context = {
        'form': form,
        'message': message
    }
    return render(request, 'Event/submitart.html', context)


def showDetails(request, comp_id):

    searched_comp = get_object_or_404(Competition, id=comp_id)
    context = {
        'search': searched_comp,

    }
    return render(request, 'Event/show_event_details.html', context)
