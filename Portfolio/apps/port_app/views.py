from django.shortcuts import render

def index(request):
    return render(request, "port_app/index.html")

def test(request):
    return render(request, "port_app/testimonials.html")

# Create your views here.
