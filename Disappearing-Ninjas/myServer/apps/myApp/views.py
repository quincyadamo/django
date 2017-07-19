# Controller
from django.shortcuts import render, redirect

# Create your views here:
def index(request):
    return render(request, 'myApp/index.html')
def turtle(request):
    context = {
        "imagesrc": "myApp/img/tmnt.png"
    }
    return render(request, 'myApp/ninjas.html', context)

def ninjas(request, ninja_color):
    # Set the default below:
    context = {
        "imagesrc": "myApp/img/AprilOneil.jpg"
    }

    if ninja_color == "blue":
        context['imagesrc'] = "myApp/img/blue.jpg"

    if ninja_color == "orange":
        context['imagesrc'] = "myApp/img/orange.jpg"

    if ninja_color == "red":
        context['imagesrc'] = "myApp/img/red.jpg"

    if ninja_color == "purple":
        context['imagesrc'] = "myApp/img/purple.jpg"

    return render(request, 'myApp/ninjas.html', context)
