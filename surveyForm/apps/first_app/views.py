from django.shortcuts import render, redirect, HttpResponse

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request, "first_app/index.html")
  
    

def survey(request):
    

    if request.method == "POST":
        request.session['yourName'] = request.POST['yourName']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        request.session['counter'] += 1
        return redirect('/results')
    
    return redirect('/')

def results(request):
    
    return render(request, "first_app/results.html")
    

# Create your views here.
