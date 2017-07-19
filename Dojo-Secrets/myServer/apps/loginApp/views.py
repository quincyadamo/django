from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here:
def index(request):
    if 'user_id' in request.session:
        return redirect(reverse('secretsApp:index'))
    else:
        return render(request, 'loginApp/index.html')

# Displays a list of all users
def all(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'loginApp/all.html', context)

def register(request):
    if request.method == 'POST':
        validation = User.objects.register(request.POST)
        if validation[0]:
            return log_user_in(request, validation[1])
        else:
            for error in validation[1]:
                messages.error(request, error)
            return redirect(reverse('users:index'))
    return redirect(reverse('users:index'))
def login(request):
    if request.method == 'POST':
        validation = User.objects.login(request.POST)
        if validation[0]:
            return log_user_in(request, validation[1])
        else:
            messages.error(request, validation[1])
    return redirect(reverse('users:index'))

def log_user_in(request, user):
    print("running log_user_in function")
    request.session['user_id'] = user.id

    # Adding user to success flash message
    messages.success(request, "Welcome, {}. You have successfully logged in!".format(user.first_name))
    return redirect(reverse('secretsApp:index'))

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        messages.success(request, "You have successfully logged out")
        return redirect(reverse('users:index'))
    else:
        messages.error(request, "You were not logged in")
        return redirect(reverse('users:index'))
