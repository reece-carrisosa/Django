from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, "first_app/index.html")

def ninjas(request):
    return render(request, "first_app/ninjas.html")

def show(request, color):
    if color == 'red':
        image = 'raphael.jpg'
    elif color == 'blue':
        image = 'leonardo.jpg'
    elif color == 'orange':
        image = 'michelangelo.jpg'
    elif color == 'purple':
        image = 'donatello.jpg'
    else:
        image = 'notapril.jpg'
    context = {
        'image': image
    }
    return render(request, "first_app/colors.html", context)
    




# Create your views here.
