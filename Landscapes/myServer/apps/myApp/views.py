from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect #, HttpResponse

# Views created below:
def index(request):
    return render(request, 'myApp/index.html')

def image(request, num):
    try:
        number = int(num)
        if number >= 1 and number <= 10:
            landscape = 'snow'
        elif number >= 11 and number <= 20:
            landscape = 'desert'
        elif number >= 21 and number <= 30:
            landscape = 'forest'
        elif number >= 31 and number <= 40:
            landscape = 'vineyard'
        elif number >= 41 and number <= 50:
            landscape = 'tropical'
        else:
            return ValueError
        context = {
            'landscape': landscape
        }
        return render(request, 'myApp/image.html', context)
    except (ValueError, AttributeError):
        messages.error(request, 'Use a number between 1 and 50 ' +
                       'as the url parameter.')
        return redirect('/')
