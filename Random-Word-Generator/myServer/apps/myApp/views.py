# This is the Controller
from __future__ import unicode_literals
import string
import random
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def generate(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    word = ''
    my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
    for times in range (0, 14):
        word = word + str(random.choice(my_letters))
    words = {
        'generate': word
    }
    return render(request, 'index.html', words)

def reset(request):
    request.session.clear()
    return redirect('/')
