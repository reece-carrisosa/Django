from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string



def index(request):
    unique_id = get_random_string(length=14)
    if 'counter' in request.session:
        pass
    else:
        request.session['counter'] = 1

    context = {
        "random_word":unique_id
        # "counter": request.session['counter']
    }
    return render(request, "first_app/index.html", context)

def generate(request):
    if request.method == "POST":
            request.session['counter'] += 1

        # try:
        #     request.session['counter'] += 1
        # except:
        #     request.session['counter'] = 1
    return redirect('/')