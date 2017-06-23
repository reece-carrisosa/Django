from django.shortcuts import render, redirect
from .models import User, Interest
# Create your views here.
def index(request):
    context = {
        "users" : User.objects.all()
    }
    return render(request, "userApp/index.html", context)

def users(request):
    User.objects.filter(name=request.POST['name'], interest=request.POST['interest'])
    return redirect('/users')

def interests(request):
    pass

def view(request):
    pass