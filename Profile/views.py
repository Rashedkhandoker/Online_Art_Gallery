from django.shortcuts import render
from .models import User
from .forms import Userform
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  # we can use all messages from 'messages' framework


# Register USer
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


def showUser(request):
    users = User.objects.all()

    context = {
        'all_users': users
    }

    return render(request, 'Profile/ShowUser.html', context)


def insertUser(request):
    form = Userform()

    message = ""
    if request.method == "POST":
        form = Userform(request.POST)
        message = "Invalid input. Please try again later."
        if form.is_valid():
            form.save()
            message = "User is added to Database."
            form = Userform()
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'profile/InsertUser.html', context)
