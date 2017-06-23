from django.shortcuts import render, HttpResponse, redirect
from .models import User
# Create your views here.
def index(request):
      print("Running index method, calling out to User.")
      user = User.objects.login("r.carrisosa@yahoo.com")
# DO NOT PASS THE WHOLE REQUEST OBJECT TO THE MODEL!!!
      print (type(user))
    #   if 'error' in user:
    #       pass
    #   if 'theuser' in user:
    #       pass
      return HttpResponse("Done running userManager method. Check your terminal console.")
