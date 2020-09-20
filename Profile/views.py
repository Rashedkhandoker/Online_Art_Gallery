from django.shortcuts import render
from .models import User
from .forms import Userform

def showUser(request):

    users = User.objects.all()

    context ={
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
