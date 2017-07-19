# Controller

from __future__ import unicode_literals
import random
from django.contrib import messages
from django.shortcuts import render, redirect #, HttpResponse

VALUES = ['wine', 'bubble bath', 'ladies night',
          'date night', 'sunshine',
          'yoga', 'cook-off', 'hike',
          '1 million dollars', 'brunch',
          'one way ticket to Bali']
SPECIFICATIONS = 'Please provide an integer from 0 to 11.'

# Create views below:
def index(request):
    return render(request, 'myApp/index.html')

def surprise(request):
    if request.method == 'POST':
        try:
            if int(request.POST['number']) == 0:
                request.session['surpriselist'] = []
                return redirect('/results')
            elif int(request.POST['number']) > 11:
                messages.error(request, SPECIFICATIONS)
                return redirect('/')
            else:
                random.shuffle(VALUES)
                # print VALUES
                surpriselist = []
                for thing in range(0, int(request.POST['number'])):
                # print SURPRISES
                    surpriselist.append(VALUES[thing])
                request.session['surpriselist'] = surpriselist
                return redirect('/results')
        except (TypeError, ValueError):
            messages.error(request, SPECIFICATIONS)
            return redirect('/')
    else:
        return redirect('/')

def results(request):
    context = {}
    context['surpriselist'] = []
    for each in range(0, len(request.session['surpriselist'])):
        context['surpriselist'].append(request.session['surpriselist'][each])

    return render(request, 'myApp/results.html', context)
