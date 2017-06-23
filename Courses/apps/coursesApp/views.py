from django.shortcuts import render, HttpResponse, redirect
from .models import Course
# Create your views here.
def index(request):
    context = {
        "courses" : Course.objects.all()
    }
    return render(request, "coursesApp/index.html", context)

def courses(request):
    Course.objects.create(courseName=request.POST['courseName'], description=request.POST['description'])
    return redirect('/')

def destroy(request, id):
    course = Course.objects.get(id=id)
    context = {
        "course" : course
    }
    return render(request, "coursesApp/courses.html", context)

def remove(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')