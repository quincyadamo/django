from __future__ import unicode_literals
from django.shortcuts import render, redirect

# Create your views here:
def index(request):
    messages = []
    return render(request, 'myApp/index.html', {'messages': messages})
