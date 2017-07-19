from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here:
def index(request):
    if 'first_name' not in request.session:
        return render(request, 'login/index.html')
    else:
        return redirect(reverse('books:home'))

def register(request):
    if User.UserManager.valid_registration(request.POST, request):
        valid = True
        user = User.objects.get(email = request.POST['email_address'])
        request.session['first_name'] = user.first_name
        request.session['user_id'] = user.id
        return redirect(reverse('books:home'))
    else:
        valid = False
        return redirect(reverse('users:index'))

def success(request):
    return redirect(request, 'books:home')

def login(request):
    if User.UserManager.exisiting_user(request.POST, request):
        valid = True
        user = User.objects.get(email = request.POST['email_address'])
        request.session['first_name'] = user.first_name
        request.session['email_address'] = user.last_name
        request.session['user_id'] = user.id
        return redirect(reverse('books:home'))
    else:
        valid = False
        return redirect(reverse('users:index'))

def logout(request):
    request.session.clear()
    return redirect(reverse('users:index'))
