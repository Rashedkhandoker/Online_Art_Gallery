<<<<<<< Updated upstream
from django.shortcuts import render,redirect
=======
from django.shortcuts import render
>>>>>>> Stashed changes
from .models import Profile
from .forms import Profileform
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  # we can use all messages from 'messages' framework
from django.contrib.auth.decorators import login_required
#Register USer

def registration(request):
    user_form = UserCreationForm()
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Account is created successfully')

    context = {
        'form': user_form,
    }

    return render(request, 'Profile/registration.html', context)


<<<<<<< Updated upstream

@login_required
def showProfile(request):

=======
def showProfile(request):

>>>>>>> Stashed changes
    profile = Profile.objects.all()

    context ={
        'Profile_list': profile
<<<<<<< Updated upstream

    }

    return render(request, 'Profile/ShowProfile.html', context)



@login_required
def createprofile(request):
    form = Profileform()


    message = ""
    if request.method == "POST":
        form = Profileform(request.POST,request.FILES)
        message = "Invalid input. Please try again later."
        if form.is_valid():
            profile = form.save(commit=False)

            profile.user = request.user

            profile.save()

            message = "Profile is Created "
=======
    }

    return render(request, 'Profile/ShowProfile.html', context)

@login_required
def createprofile(request):
    form = Profileform()

    message = ""
    if request.method == "POST":
        form = Profileform(request.POST)
        message = "Invalid input. Please try again later."
        if form.is_valid():
            form.save()
            message = "User is added to Database."
>>>>>>> Stashed changes
            form = Profileform()
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'profile/CreateProfile.html', context)
