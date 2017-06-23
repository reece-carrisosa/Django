from django.shortcuts import render, HttpResponse
from datetime import datetime


def index(request):
    context = {
        "date":datetime.now().date(),
        "time":datetime.now().time()

    }
    return render(request, "first_app/index.html", context)

# Create your views here.
