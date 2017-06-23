from django.shortcuts import render, HttpResponse, redirect
from .models import Book
# Create your views here.
def index(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, "bookApp/index.html", context)

def books(request):
    Book.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])
    return redirect('/')