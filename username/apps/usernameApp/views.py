from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):

    return render(request, "usernameApp/index.html")

def success(request):
    context = {
        "username" : User.objects.all()
    }

    if request.method == 'POST':
        answer = User.objects.validuser(request.POST['user'])
        if answer["status"]:
            user = answer["data"]
            messages.add_message(request, messages.SUCCESS, 'Username {} is Valid!'.format(user))
            return render(request, "usernameApp/success.html", context)

        else:
            for errors in answer["data"]:
                messages.add_message(request, messages.ERROR, 'Username {}'.format(errors))
            return redirect('/')