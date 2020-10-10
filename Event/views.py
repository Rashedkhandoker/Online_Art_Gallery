from django.shortcuts import render, get_object_or_404

from .models import Competition,SubmitCompetition
from .forms import SubmitCompetitionForm,ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def showcompetition(request):
    competition  = Competition.objects.all()
    if request.method == 'POST':
        competition =Competition.objects.filter(title__icontains=request.POST['search'])
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




@login_required()
def showSubmission(request):

    Artsubmission = SubmitCompetition.objects.all()

    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            searched_product.reviews.add(instance)
            searched_product.save()
    context ={
        'all_submission': Artsubmission,
        'form': form
    }
    return render(request,'Event/showsubmission.html', context)


@login_required
def review_after_complete(request, art_id):

    already_reviewed = False

    searched_product = get_object_or_404(Product, id=art_id)

    user_list = searched_product.reviews.filter(user=request.user)
    print(user_list, len(user_list))
    if len(user_list) != 0:
        already_reviewed = True


    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            searched_product.reviews.add(instance)
            searched_product.save()

            return redirect('my-orders')

    context = {
        'search': searched_product,
        'form': form,
        'already_reviewed': already_reviewed
    }
    return render(request, 'ProductManagement/detail_product_view_review.html', context)

def showArtDetails(request,s_id):

    searched_s = get_object_or_404(SubmitCompetition, id=s_id)
    context = {
        'search': searched_s,


    }
    return render(request, 'Event/show_art_details.html', context)