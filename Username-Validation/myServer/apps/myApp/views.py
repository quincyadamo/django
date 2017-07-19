from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Username

# Create your views here:
def index(request):
    return render(request, 'myApp/index.html')

def validate(request):
    if request.method=='POST':
        if Username.objects.validate(request.POST['username']):
            Username.objects.create(name=request.POST['username'])
            messages.success(
                request,
                'The username you entered, ' + request.POST['username'] +
                ', is valid. Thank you!'
            )
            return redirect('/success')
        else:
            messages.error(
                request,
                'Username is not valid!'
            )
    return redirect('/')

def success(request):
    context = {
        'usernamelist': Username.objects.all()
    }
    return render(request, 'myApp/success.html', context)
