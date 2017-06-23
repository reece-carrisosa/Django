from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
    if 'goldsum' not in request.session:
        request.session['goldsum'] = 0
    return render(request, "first_app/index.html")

def process_money(request):
    request.session['activity'] = []
    bldg = request.POST['bldg']
    if bldg == 'farm':
        request.session['goldsum'] += random.randrange(10,20)
        request.session['activity'].append(request.session['goldsum'])

    if bldg == 'cave':
        request.session['goldsum'] += random.randrange(5,10)
        request.session['activity'].append(request.session['goldsum'])

    if bldg == 'house':
        request.session['goldsum'] += random.randrange(2,5)
        request.session['activity'].append(request.session['goldsum'])

    elif bldg == 'casino':
        request.session['goldsum'] = random.randrange(-50,50)
        if request.session['goldsum'] >= 0:
            request.session['activity'].append(request.session['goldsum'])
        else:
            request.session['activity'].append(request.session['goldsum'])
    return render(request, "first_app/index.html")

def reset(request):
    request.session.clear()
    return redirect('/')


# Create your views here.
