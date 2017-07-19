from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here:
def index(request):
    if 'user_id' in request.session:
        return redirect(reverse('all'))
    else:
        return render(request, 'myApp/index.html')

# A list of all users:
def all(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'myApp/all.html', context)

def register(request):
    if request.method == 'POST':
        validation = User.objects.register(request.POST)
        if validation[0]:
            return log_user_in(request, validation[1])
        else:
            for error in validation[1]:
                messages.error(request, error)
            return redirect(reverse('index'))
    return redirect(reverse('index'))

def login(request):
    if request.method == 'POST':
        validation = User.objects.login(request.POST)
        if validation[0]:
            return log_user_in(request, validation[1])
        else:
            messages.error(request, validation[1])
    return redirect(reverse('index'))

def log_user_in(request, user):
    print("running log-user-in function")
    request.session['user_id'] = user.id

    # To add user to success flash message
    messages.success(request, "Success! Welcome, {}. You are logged in.".format(user.first_name))
    return redirect(reverse('all'))

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        messages.success(request, "You have been successfully logged out")
        return redirect(reverse('index'))
    else:
        messages.error(request, "You were not logged in")
        return redirect(reverse('index'))
