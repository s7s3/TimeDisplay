from django.shortcuts import render, HttpResponse , redirect
from time import gmtime, strftime

def red_to_timeDisplay(request):
    return redirect("/timeDisplay")

def index(request):
    context = {
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%H:%M %p", gmtime())
    }
    return render(request, 'index.html', context)